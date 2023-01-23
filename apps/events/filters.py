from django_filters import FilterSet, ChoiceFilter, CharFilter
from django import forms

from . models import Event

class EventFilter(FilterSet):

    name = CharFilter(
        lookup_expr="icontains", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    school = ChoiceFilter(
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Event
        fields = ["name","school"]