from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse
from rolepermissions.roles import assign_role
from braces.views import GroupRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import UpdateView,DetailView,ListView

from . form import RegisterForm,UpdateForm,UpdateTypeUser
from . models import User
from apps.documents.models import Memorando,Official,Requeriment
from apps.events.models import Event
from . filters import UserFilter
# Create your views here.
class Home(LoginRequiredMixin, TemplateView):
    template_name = "users/dashboard.html"


class Register(View):
    form_class = RegisterForm
    initial = {"key": "value"}
    template_name = "users/register.html"

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': self.form_class})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            typeUser = form.cleaned_data.get("typeUser")
            email = form.cleaned_data.get("email")
            user = User.objects.get(email=email)
            if typeUser == "secretary":
                assign_role(user,'secretary')
            if typeUser == "coordinator":
                assign_role(user,'coordinator')
            if typeUser == "asg":
                assign_role(user,'asg')
            if typeUser == "fooddivider":
                assign_role(user,'fooddivider')
            if typeUser == "nutricionist":
                assign_role(user,'nutricionist')
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            return redirect(to="/")
        return render(request, self.template_name, {'form': form})


class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("dashboard")

    def form_invalid(self, form):
        messages.error(self.request, "Inválido Login e Senha.")
        return self.render_to_response(self.get_context_data(form=form))

class LogoutView(View):
    def get(self, request):
        logout(request)
        return reverse("login")

class DetailPerfil(LoginRequiredMixin,DetailView):
    model = User
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'user'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['memorandos'] = Memorando.objects.filter(user = self.request.user).count()
        context['officials'] = Official.objects.filter(user = self.request.user).count()
        context['requeriments'] = Requeriment.objects.filter(user = self.request.user).count()
        context['events'] = Event.objects.filter(status_activated = False)
        return context
    

class UpdatePerfil(LoginRequiredMixin,UpdateView):
    model = User
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    form_class = UpdateForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uuid'] = self.kwargs.get('uuid')
        return context



    success_url = reverse_lazy("dashboard")

class AdminUsers(GroupRequiredMixin,LoginRequiredMixin,ListView):
    group_required = [u"secretary", u"coordinator"]
    model = User
    context_object_name = 'user_list'
    filterset = UserFilter
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset().all().order_by('username')
        self.filterset = self.filterset(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context

@login_required

def updateTypeUser(request,uuid):

    if request.method == 'GET':

        typeUser = request.GET['typeUser']
        user = User.objects.get(uuid = uuid)
        user.typeUser = typeUser
        user.save()
        if user.typeUser == 'asg':
            assign_role(user,'asg')
        if user.typeUser == 'coordenador':
            assign_role(user,'coordinator')
        if user.typeUser == 'fooddivider':
            assign_role(user,'fooddivider')
        if user.typeUser == 'nutricionist':
            assign_role(user,'nutricionist')
        if user.typeUser == 'secretary':
            assign_role(user,'secretary')
        print(typeUser)
        return redirect('/users/adminusers/')