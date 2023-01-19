from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
# Create your views here.
from . models import Food, Cleaning, Request_Food, Request_Cleaning
from . forms import FoodForm, CleaningForm, RequestFoodForm, RequestCleaningForm,FoodFormUpdate

# views of Food

class FoodCreateView(LoginRequiredMixin, CreateView):

    model = Food
    form_class = FoodForm
    template_name = 'products/food_form.html'
    success_url = reverse_lazy("products:food_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(FoodCreateView,self).form_valid(form)

class FoodListView(LoginRequiredMixin, ListView):

    model = Food
    context_object_name = 'food_list'
    def get_queryset(self):
        user = self.request.user
        return Food.objects.filter(user = user)
    paginate_by = 10

class FoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Food
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    form_class  = FoodFormUpdate
    success_url = reverse_lazy("products:food_list")

class FoodDeleteView(LoginRequiredMixin, DeleteView):
    model = Food
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'foods'
    success_url = reverse_lazy('products:food_list')

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(FoodDeleteView,self).form_valid(form)

#views of cleaning

class CleaningCreateView(LoginRequiredMixin, CreateView):

    model = Cleaning
    form_class = CleaningForm
    template_name = 'products/cleaning_form.html'
    success_url = reverse_lazy("products:cleaning_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(CleaningCreateView,self).form_valid(form)

class CleaningListView(LoginRequiredMixin, ListView):

    model = Cleaning
    context_object_name = 'cleaning_list'
    def get_queryset(self):
        user = self.request.user
        return Cleaning.objects.filter(user = user)
    paginate_by = 10

class CleaningUpdateView(LoginRequiredMixin, UpdateView):
    model = Cleaning
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    form_class  = CleaningForm
    success_url = reverse_lazy("products:cleaning_list")

class CleaningDeleteView(LoginRequiredMixin, DeleteView):
    model = Cleaning
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'cleaning'
    success_url = reverse_lazy('products:cleaning_list')

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(CleaningDeleteView,self).form_valid(form)

class RequestFoodCreateView(LoginRequiredMixin, CreateView):

    model = Request_Food
    form_class = RequestFoodForm
    # fields = ['food','quantity']
    template_name = 'products/requestfood_form.html'
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(RequestFoodCreateView,self).form_valid(form)