from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,DetailView
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# from crum import get_current_user
# Create your views here.
from . models import Food, Cleaning, Request_Food, Request_Cleaning, Food_RequestFood,Cleaning_RequestCleaning
from . forms import FoodForm, CleaningForm, RequestFoodForm, RequestCleaningForm,FoodFormUpdate
from . filters import FoodFilter,CleaningFilter
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
    filterset= FoodFilter
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        self.filterset = self.filterset(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context

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
    paginate_by = 10
    filterset = CleaningFilter
    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        self.filterset = self.filterset(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context

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

#Request Food
class RequestFoodCreateView(LoginRequiredMixin, CreateView):

    model = Request_Food
    form_class = RequestFoodForm
    # fields = ['food','quantity']
    template_name = 'products/requestfood_form.html'
    success_url = reverse_lazy("products:request_food_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(RequestFoodCreateView,self).form_valid(form)

class RequestFoodListView(LoginRequiredMixin, ListView):

    model = Request_Food
    context_object_name = 'requestfoods'
    def get_queryset(self):
        user = self.request.user
        return Request_Food.objects.filter(user = user)
    paginate_by = 10

class RequestFoodDetailsView(LoginRequiredMixin, DetailView):
    
    model = Request_Food
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'request_food'
    filterset= FoodFilter
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foods"] = Food.objects.exclude(quantity = 0)
        context["list_food_request_table"] = Food_RequestFood.objects.filter(requestfood = self.kwargs.get("uuid"))
        self.filterset = self.filterset(self.request.GET, queryset=context['foods'])
        context['foods'] = self.filterset.qs
        context['form_filter'] = self.filterset.form
        return context


@login_required
def request_food(request,uuid_request,uuid_food):
    if request.method == 'GET':
        quantity = request.GET.get('quantity')
        request_food = Request_Food.objects.get(uuid = uuid_request)
        food = Food.objects.get(uuid = uuid_food)
        print(uuid_food)
        request_food_table = Food_RequestFood(
            quantity = quantity,
            requestfood = request_food,
            food = food
        )
        request_food_table.save()

        return redirect(f"/products/requestfooddetail/{uuid_request}/")
    return redirect("/")

# Request Cleaning
class RequestCleaningCreateView(LoginRequiredMixin, CreateView):

    model = Request_Cleaning
    form_class = RequestCleaningForm
    template_name = 'products/requestcleaning_form.html'
    success_url = reverse_lazy("products:request_cleaning_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(RequestCleaningCreateView,self).form_valid(form)

class RequestCleadingListView(LoginRequiredMixin, ListView):

    model = Request_Cleaning
    context_object_name = 'request_cleaning_list'
    def get_queryset(self):
        user = self.request.user
        return Request_Cleaning.objects.filter(user = user)
    paginate_by = 10

class RequestCleaningDetailView(LoginRequiredMixin, DetailView):

    model = Request_Cleaning
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'request_cleaning_detail'
    filterset= CleaningFilter
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cleanings"] = Cleaning.objects.exclude(quantity = 0)
        context["list_cleaning_request_table"] = Cleaning_RequestCleaning.objects.filter(requestcleaning = self.kwargs.get("uuid"))
        self.filterset = self.filterset(self.request.GET, queryset=context['cleanings'])
        context['cleanings'] = self.filterset.qs
        context['form_filter'] = self.filterset.form
        return context
def request_cleaning(request,uuid_request,uuid_cleaning):
    if request.method == 'GET':
        quantity = request.GET.get('quantity')
        request_cleaning = Request_Cleaning.objects.get(uuid = uuid_request)
        cleaning = Cleaning.objects.get(uuid = uuid_cleaning)
        print(uuid_cleaning)
        request_cleaning_table = Cleaning_RequestCleaning(
            quantity = quantity,
            requestcleaning= request_cleaning,
            cleaning = cleaning
        )
        request_cleaning_table.save()

        return redirect(f"/products/requestcleaningdetail/{uuid_request}/")
    return redirect("/")