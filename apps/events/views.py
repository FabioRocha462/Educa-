from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,DetailView
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# Create your views here.
from . models import Event
from . forms import EventForm
from . filters import EventFilter

class EventsCreateView(LoginRequiredMixin,CreateView):

    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy("events:event_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(EventsCreateView,self).form_valid(form)

class EventsListView(LoginRequiredMixin, ListView):

    model = Event
    context_object_name = 'event_list'
    filterset= EventFilter
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        self.filterset = self.filterset(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context