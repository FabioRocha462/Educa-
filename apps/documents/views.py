from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,DetailView
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

# Create your views here.
from . models import Memorando,Official
from . forms import MemorandoForm,OfficialForm
from . filters import MemorandoFilter,OfficialFilter
import datetime
#views memorando
class MemorandoCreateView(LoginRequiredMixin, CreateView):

    model = Memorando
    form_class = MemorandoForm
    template_name = "documents/memorando_form.html"
    success_url = reverse_lazy("documents:memorando_list")

    def form_valid(self, form):
        year = datetime.date.today().year
        memorandos = Memorando.objects.filter(created_at__year=year)
        form.instance.number = len(memorandos) + 1
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(MemorandoCreateView,self).form_valid(form)

class MemorandoListView(LoginRequiredMixin, ListView):

    model = Memorando
    context_object_name = 'memorando_list'
    filterset= MemorandoFilter
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        self.filterset = self.filterset(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context

class MemorandoDetailView(LoginRequiredMixin, DetailView):

    model = Memorando
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'memorando'
   

# views Official

class OfficialCreateView(LoginRequiredMixin, CreateView):

    model = Official
    form_class = OfficialForm
    template_name = "documents/official_form.html"
    success_url = reverse_lazy("documents:official_list")

    def form_valid(self, form):
        year = datetime.date.today().year
        officials = Official.objects.filter(created_at__year=year)
        form.instance.number = len(officials) + 1
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(OfficialCreateView,self).form_valid(form)

class OfficialListView(LoginRequiredMixin, ListView):

    model = Official
    context_object_name = 'official_list'
    filterset = OfficialFilter
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        self.filterset = self.filterset(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context