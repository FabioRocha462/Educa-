from django_filters import FilterSet, ChoiceFilter, CharFilter
from django import forms
from . models import User
choices = (
        ('secretary','Secretary'),
        ('asg','Asg'),
        ('coordinator','Coordinator'),
        ('nutricionist','Nutricionist'),
        ('food_divider','Food Divider'),
    )
class UserFilter(FilterSet):

    username = CharFilter(
        lookup_expr="icontains", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    typeUser = ChoiceFilter(
        choices=choices,widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ['username', 'typeUser']