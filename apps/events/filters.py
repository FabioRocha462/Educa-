from django_filters import FilterSet, ChoiceFilter, CharFilter
from django import forms

from . models import Event
choices = (
        ("1","04 de Outubro"),
        ("2","Pequeno Mário"),
        ("3","Ariamiro"),
        ("4","Maria Dália"),
        ("5","Baixa do Fogo"),
        ("6","Serra"),
        ("7","Angicos"),
        ("8","Jerimum"),
        ("9","Ema"),
        ("10","Carnaubinha")
        )
class EventFilter(FilterSet):

    name = CharFilter(
        lookup_expr="icontains", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    school = ChoiceFilter(
       choices=choices,widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Event
        fields = ["name","school"]