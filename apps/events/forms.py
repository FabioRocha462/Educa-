from django import forms
from django.forms import ModelForm, inlineformset_factory

from . models import Event, Food_Event
class EventForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:

        model = Event
        fields = [
            "name",
            "school",
            "date",
        ]

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'school': forms.RadioSelect(attrs={'class': 'form-control', 'type':'radio'}),
        }

class FoodEventForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:

        model = Food_Event
        fields = [
            'quantity',
        ]


