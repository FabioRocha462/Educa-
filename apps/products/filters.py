from django_filters import FilterSet, ChoiceFilter, CharFilter
from django import forms

from . models import Food,Cleaning
class FoodFilter(FilterSet):

    name = CharFilter(
        lookup_expr="icontains", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Food
        fields = ["name"]

class CleaningFilter(FilterSet):

    name = CharFilter(
        lookup_expr="icontains", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Cleaning
        fields = ["name"]
