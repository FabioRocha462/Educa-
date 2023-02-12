from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,DetailView
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from braces.views import GroupRequiredMixin
# Create your views here.
from . models import Memorando,Official, Requeriment
from . forms import MemorandoForm,OfficialForm,RequerimentsForm
from . filters import MemorandoFilter,OfficialFilter,RequirementFilter
import datetime
from django.http import FileResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

#views memorando
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------


class MemorandoCreateView(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    group_required = [u"secretary",u"coordinator",u"nutricionist",u"fooddivider"]
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

class MemorandoListView(GroupRequiredMixin,LoginRequiredMixin, ListView):
    group_required = [u"secretary",u"coordinator",u"nutricionist",u"fooddivider"]
    model = Memorando
    context_object_name = 'memorando_list'
    filterset= MemorandoFilter
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset().all().order_by('created_at')
        self.filterset = self.filterset(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context

class MemorandoDetailView(GroupRequiredMixin,LoginRequiredMixin, DetailView):

    group_required = [u"secretary",u"coordinator",u"nutricionist",u"fooddivider"]
    model = Memorando
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'memorando'




class MemorandoUpdateView(GroupRequiredMixin,LoginRequiredMixin,UpdateView):

    group_required = [u"secretary",u"coordinator",u"nutricionist",u"fooddivider"]
    model = Memorando
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    form_class = MemorandoForm
    success_url = reverse_lazy("documents:memorando_list")


@login_required
def confirming_memorando(request,uuid):

    if request.method == "GET":

        memorando = Memorando.objects.get(uuid=uuid)
        memorando.confirm = True
        memorando.save()
        return redirect("/documents/memorandolist/")
    return redirect("/")
@login_required
def generate_pdf_memorando(request,pk):
    memorando = Memorando.objects.get(pk=pk)
    return render(request, 'documents/memorandoreport.html',{'memorando':memorando}) 


# views Official
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------

class OfficialCreateView(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    group_required = [u"secretary",u"coordinator",u"nutricionist",u"fooddivider"]
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

class OfficialListView(GroupRequiredMixin,LoginRequiredMixin, ListView):
    group_required = [u"secretary",u"coordinator",u"nutricionist",u"fooddivider"]
    model = Official
    context_object_name = 'official_list'
    filterset = OfficialFilter
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset().all().order_by('created_at')
        self.filterset = self.filterset(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context

class OfficialDetailView(GroupRequiredMixin,LoginRequiredMixin, DetailView):
    group_required = [u"secretary",u"coordinator",u"nutricionist",u"fooddivider"]
    model = Official
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'official'

class OfficialUpdateView(GroupRequiredMixin,LoginRequiredMixin,UpdateView):

    group_required = [u"secretary",u"coordinator",u"nutricionist",u"fooddivider"]
    model = Official
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    form_class = OfficialForm
    success_url = reverse_lazy("documents:official_list")

@login_required
def confirming_official(request,uuid):

    if request.method == "GET":

        official = Official.objects.get(uuid=uuid)
        official.confirm = True
        official.save()
        return redirect("/documents/officiallist/")
    return redirect("/")
# views Requirements
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
class RequerimentCreateView(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    group_required = [u"secretary",u"coordinator",u"nutricionist",u"fooddivider",u"asg"]
    model = Requeriment
    form_class = RequerimentsForm
    template_name = "documents/requeriment_form.html"
    success_url = reverse_lazy("documents:requeriment_list")

    def form_valid(self, form):
        year = datetime.date.today().year
        requeriment = Requeriment.objects.filter(created_at__year=year)
        form.instance.number = len(requeriment) + 1
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(RequerimentCreateView,self).form_valid(form)

class RequerimentListView(GroupRequiredMixin,LoginRequiredMixin, ListView):
    group_required = [u"secretary",u"coordinator",u"nutricionist",u"fooddivider",u"asg"]
    model = Requeriment
    context_object_name = 'requeriment_list'
    filterset = RequirementFilter
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset().all().order_by('created_at')
        self.filterset = self.filterset(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context

class RequerimentDetailView(GroupRequiredMixin,LoginRequiredMixin, DetailView):
    group_required = [u"secretary",u"coordinator",u"nutricionist",u"fooddivider",u"asg"]
    model = Requeriment
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'requeriment'

class RequerimentUpdateView(GroupRequiredMixin,LoginRequiredMixin,UpdateView):

    group_required = [u"secretary",u"coordinator",u"nutricionist",u"fooddivider"]
    model = Requeriment
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    form_class = RequerimentsForm
    success_url = reverse_lazy("documents:requeriment_list")

@login_required
def confirming_requeriment(request,uuid):

    if request.method == "GET":

       requeriment = Requeriment.objects.get(uuid=uuid)
       requeriment.confirm = True
       requeriment.save()
       return redirect("/documents/requerimentlist/")
    return redirect("/")