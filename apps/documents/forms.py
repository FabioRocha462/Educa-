from django import forms
from django.forms import ModelForm, inlineformset_factory

from . models import Memorando, Official, Requeriment

class MemorandoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MemorandoForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:

        model = Memorando
        fields = [
            'others',
            'receiver',
            "destiny",
            "description",
        ]
        widgets = {
            'destiny': forms.RadioSelect(attrs={'class': 'form-control', 'type':'radio'}),
        }        

class OfficialForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(OfficialForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:

        model = Memorando
        fields = [
            'others',
            'receiver',
            "destiny",
            "description",
        ]

        widgets = {
            'destiny': forms.RadioSelect(attrs={'class': 'form-control', 'type':'radio'}),
        } 


class RequerimentsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(RequerimentsForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:

        model = Memorando
        fields = [
            'others',
            'receiver',
            "destiny",
            "description",
        ]

        widgets = {
            'destiny': forms.RadioSelect(attrs={'class': 'form-control', 'type':'radio'}),
        } 