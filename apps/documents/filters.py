from django_filters import FilterSet, ChoiceFilter, CharFilter,DateFilter 
from django import forms

from . models import Memorando,Official

class MemorandoFilter(FilterSet):

    created_at = DateFilter(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type':'date'})
    )

    class Meta:
        model = Memorando
        fields = ["created_at"]

class OfficialFilter(FilterSet):

    created_at = DateFilter(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type':'date'})
    )

    class Meta:
        model = Official
        fields = ["created_at"]
    