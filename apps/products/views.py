from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,DetailView
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from braces.views import GroupRequiredMixin
# from crum import get_current_user
# Create your views here.
from . models import Food, Cleaning, Request_Food, Request_Cleaning, Food_RequestFood,Cleaning_RequestCleaning
from . forms import FoodForm, CleaningForm, RequestFoodForm, RequestCleaningForm,FoodFormUpdate
from . filters import FoodFilter,CleaningFilter
# views of Food

class FoodCreateView(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    group_required = u"fooddivider"
    model = Food
    form_class = FoodForm
    template_name = 'products/food_form.html'
    success_url = reverse_lazy("products:food_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(FoodCreateView,self).form_valid(form)

class FoodListView(GroupRequiredMixin,LoginRequiredMixin, ListView):
    model = Food
    group_required = [u"fooddivider",u"secretary",u"nutricionist"]
    context_object_name = 'food_list'
    filterset= FoodFilter
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset().all().order_by("name")
        self.filterset = self.filterset(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context

class FoodUpdateView(GroupRequiredMixin,LoginRequiredMixin, UpdateView):
    group_required = u"fooddivider"
    model = Food
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    form_class  = FoodFormUpdate
    success_url = reverse_lazy("products:food_list")

class FoodDeleteView(GroupRequiredMixin,LoginRequiredMixin, DeleteView):
    group_required = u"fooddivider"
    model = Food
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'foods'
    success_url = reverse_lazy('products:food_list')

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(FoodDeleteView,self).form_valid(form)

class FoodDetailView(GroupRequiredMixin,LoginRequiredMixin, DetailView):

    group_required = [u"fooddivider",u"nutricionist",u"secretary"]
    model = Food
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'food'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "quantity" in self.request.GET:
            quantity = self.request.GET["quantity"]
            quantity = float(quantity)
            food = Food.objects.get(uuid = self.kwargs.get("uuid"))
            if food.quantity < quantity:
                messages.error(self.request, "A quantidade repassada é maior que a quantidade do produto. :(")
                context['food'] = food
                return context
            else:
                food.quantity = food.quantity - quantity
                food.save()
                messages.success(self.request,"Atualizado com sucesso :)")
                context['food'] = food
                return context

        else:
            return context    

class FoodPrint(GroupRequiredMixin,LoginRequiredMixin,ListView):
    group_required = u"fooddivider"
    model  = Food
    context_object_name = 'foods'
    def get_queryset(self):
        queryset = super().get_queryset().all().order_by("name")
        return queryset

#views of cleaning

class CleaningCreateView(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    group_required = u"fooddivider"
    model = Cleaning
    form_class = CleaningForm
    template_name = 'products/cleaning_form.html'
    success_url = reverse_lazy("products:cleaning_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(CleaningCreateView,self).form_valid(form)

class CleaningListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"fooddivider",u"secretary",u"nutricionist"]
    model = Cleaning
    context_object_name = 'cleaning_list'
    paginate_by = 10
    filterset = CleaningFilter
    def get_queryset(self):
        queryset = super().get_queryset().all().order_by("name")
        self.filterset = self.filterset(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context

class CleaningUpdateView(GroupRequiredMixin,LoginRequiredMixin, UpdateView):
    group_required = u'fooddivider'
    model = Cleaning
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    form_class  = CleaningForm
    success_url = reverse_lazy("products:cleaning_list")

class CleaningDeleteView(GroupRequiredMixin,LoginRequiredMixin, DeleteView):
    group_required = u"fooddivider"
    model = Cleaning
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'cleaning'
    success_url = reverse_lazy('products:cleaning_list')

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(CleaningDeleteView,self).form_valid(form)

class CleaningDetailView(GroupRequiredMixin,LoginRequiredMixin, DetailView):
    group_required = [u"fooddivider",u"nutricionist",u"secretary"]
    model = Cleaning
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'cleaning'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "quantity" in self.request.GET:
            quantity = self.request.GET["quantity"]
            quantity = float(quantity)
            cleaning = Cleaning.objects.get(uuid = self.kwargs.get("uuid"))
            if cleaning.quantity < quantity:
                messages.error(self.request, "A quantidade repassada é maior que a quantidade do produto.")
                context['cleaning'] = cleaning
            else:
                cleaning.quantity = cleaning.quantity - quantity
                cleaning.save()
                messages.success(self.request,"Atualizado com sucesso")
                context['cleaning'] = cleaning
        return context

#Request Food
class RequestFoodCreateView(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    group_required = [u"asg",u"nutricionist","secretary"]
    model = Request_Food
    form_class = RequestFoodForm
    # fields = ['food','quantity']
    template_name = 'products/requestfood_form.html'
    success_url = reverse_lazy("products:request_food_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(RequestFoodCreateView,self).form_valid(form)

class RequestFoodListView(GroupRequiredMixin,LoginRequiredMixin, ListView):
    group_required = [u"asg",u"nutricionist","secretary"]
    model = Request_Food
    context_object_name = 'requestfoods'
    def get_queryset(self):
        user = self.request.user
        return Request_Food.objects.filter(user = user)
    paginate_by = 10

class RequestFoodDetailsView(GroupRequiredMixin,LoginRequiredMixin, DetailView):
    group_required = [u"asg",u"fooddivider"]
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

@login_required
def confirm_request_food(request,uuid):
    if request.method == 'GET':

        request_food = Request_Food.objects.get(uuid = uuid)
        request_food.status_activate = True
        request_food.save()
        return redirect(f"/users/details/{request.user.uuid}/")
    return redirect("/")

# Request Cleaning
class RequestCleaningCreateView(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    group_required = u"asg"
    model = Request_Cleaning
    form_class = RequestCleaningForm
    template_name = 'products/requestcleaning_form.html'
    success_url = reverse_lazy("products:request_cleaning_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(RequestCleaningCreateView,self).form_valid(form)

class RequestCleadingListView(GroupRequiredMixin,LoginRequiredMixin, ListView):
    group_required = [u"asg", u"secretary"]
    model = Request_Cleaning
    context_object_name = 'request_cleaning_list'
    def get_queryset(self):
        user = self.request.user
        return Request_Cleaning.objects.filter(user = user)
    paginate_by = 10

class RequestCleaningDetailView(GroupRequiredMixin,LoginRequiredMixin, DetailView):
    group_required = u"asg"
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

@login_required
def confirm_request_cleaning(request,uuid):
    if request.method == 'GET':

        request_cleaning = Request_Cleaning.objects.get(uuid = uuid)
        request_cleaning.status_activate = True
        request_cleaning.save()
        return redirect(f"/users/details/{request.user.uuid}/")
    return redirect("/")