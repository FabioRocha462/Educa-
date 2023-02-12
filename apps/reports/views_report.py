from apps.products.models import Food, Cleaning
from apps.documents.models import Memorando,Requeriment,Official
from apps.events.models import Event

from django.http import FileResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import connection
import datetime
from django.contrib import messages
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import FileResponse
from io import BytesIO
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt

# Create your views here.
class ReportView(LoginRequiredMixin, TemplateView):
    template_name = "reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "date" in self.request.GET:
            date = self.request.GET["date"]
            foods = Food.objects.filter(validity__lte = date)
            messages.success(self.request, "Feita com sucesso.")
            context["foods"] = foods

        if "dateInit" in self.request.GET and "dateEnd" in self.request.GET and "document" in self.request.GET:
            dateInit = self.request.GET["dateInit"]
            dateEnd = self.request.GET["dateEnd"]
            if dateInit > dateEnd:
                messages.error(self.request, "A data de ínicio não pode ser maior que a data final.")
            else:

                typeDocument = self.request.GET["document"]
                if typeDocument == "memorando":
                   memorandos = Memorando.objects.filter(created_at__range = [dateInit, dateEnd])
                   context["documents"] = memorandos
                if  typeDocument == "official":
                   official = Official.objects.filter(created_at__range = [dateInit, dateEnd])
                   context["documents"] = official
                if  typeDocument == "requeriment":
                   requeriments = Requeriment.objects.filter(created_at__range = [dateInit, dateEnd])
                   context["documents"] = requeriments

                messages.success(self.request, "Feita com sucesso.")
        if "school" in self.request.GET:
            school = self.request.GET["school"]
            events = Event.objects.filter(school = school )
            context["events"] = events
        return context

@login_required
def search_with_sql(request,nameFood):

     cursor = connection.cursor()
     cursor.execute("SELECT * FROM products_food WHERE name = %s", [nameFood])
     row = cursor.fetchone()
     return JsonResponse({"row" : row})

def graphic(request):
    listCategorys = []
    sumValue = []
    cursor = connection.cursor()
    cursor.execute("SELECT typeCategoria, SUM(bidding_value) FROM products_food GROUP BY typeCategoria")
    rows = cursor.fetchall()
    for row in rows:
        listCategorys.append(row[0])
        sumValue.append(row[1])
    fig, ax = plt.subplots()
    ax.pie(sumValue,labels=listCategorys,autopct='%1.1f%%', shadow=True,startangle=90)
    ax.axis('equal')
    plt.savefig("bargraph.png")
    return FileResponse(open("bargraph.png", "rb"), content_type="image/png")
    
    