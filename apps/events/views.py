from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,DetailView
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from braces.views import GroupRequiredMixin
# Create your views here.
from . models import Event, Food_Event
from . forms import EventForm
from . filters import EventFilter
from apps.products.models import Food
from apps.products.filters import FoodFilter


class EventsCreateView(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    group_required = [u"secretary", u"coordinator",u"nutricionist"]
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy("events:event_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(EventsCreateView,self).form_valid(form)

class EventsListView(GroupRequiredMixin,LoginRequiredMixin, ListView):
    group_required = [u"secretary", u"coordinator",u"nutricionist",u"fooddivider"]
    model = Event
    context_object_name = 'event_list'
    filterset= EventFilter
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset().all().order_by("name")
        self.filterset = self.filterset(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context

class EventsUpdateView(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    group_required = [u"secretary", u"coordinator", u"nutricionist"]
    model = Event
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    form_class  = EventForm
    success_url = reverse_lazy("events:event_list")


class EventsDeleteView(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    group_required = [u"secretary", u"coordinator", u"nutricionist"]
    model = Event
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'events'
    success_url = reverse_lazy('events:event_list')

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(EventsDeleteView,self).form_valid(form)

class EventsDetailView(GroupRequiredMixin,LoginRequiredMixin,DetailView):
    group_required = [u"secretary", u"coordinator",u"nutricionist",u"fooddivider"]
    model = Event
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'event'
    filterset= FoodFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foods"] = Food.objects.exclude(quantity = 0)
        context["food_event"] = Food_Event.objects.filter(event = self.kwargs.get("uuid"))
        self.filterset = self.filterset(self.request.GET, queryset=context['foods'])
        context['foods'] = self.filterset.qs
        context['form_filter'] = self.filterset.form
        return context

@login_required
def food_event(request,uuid_event,uuid_food):

    if request.method == 'GET':

        quantity = request.GET.get('quantity')
        food = Food.objects.get(uuid = uuid_food)
        event = Event.objects.get(uuid = uuid_event)
        food_event = Food_Event(
            food = food,
            event = event,
            quantity = quantity,
            user = request.user
        )

        food_event.save()
        messages.success(request, "The event was confirmed successfully.")
        return redirect(f"/events/eventsdetail/{uuid_event}/")
    return redirect("/")

@login_required
def confirmEvent(request,uuid_event):

    if request.method == 'GET':

        event = Event.objects.get(uuid = uuid_event)
        event.status_activated = True
        event.save()

        return redirect(f"/users/details/{request.user.uuid}/")
    return redirect("/")