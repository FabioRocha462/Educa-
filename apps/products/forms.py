from django import forms
from django.forms import ModelForm, inlineformset_factory
from . models import Food,Cleaning, Request_Food, Request_Cleaning

class FoodForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:

        model = Food
        fields = [
            "name",
            "quantity",
            "validity",
            "bidding_value",
            "typeCategoria",
        ]

        widgets = {
            'validity': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }



class CleaningForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CleaningForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:

        model = Cleaning
        fields = [
            "name",
            "quantity",
        ]

class RequestFoodForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RequestFoodForm, self).__init__(*args, **kwargs)
            
        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'form-control'  

    class Meta:

        model = Request_Food
        fields = [
            'name',
        ]
        


class RequestCleaningForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(RequestCleaningForm, self).__init__(*args, **kwargs)
            
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'  

    class Meta:

        model = Request_Cleaning
        fields = [
            'name',
        ]

        widgets = {
            'cleaning': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'type':'checkbox'}),
        }


class FoodFormUpdate(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FoodFormUpdate, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields["validity"].widget.attrs["disabled"] = False
        self.fields["typeCategoria"].widget.attrs["disabled"] = False


    class Meta:

        model = Food
        fields = [
            "name",
            "quantity",
            "validity",
            "typeCategoria",
            "bidding_value",
        ]

    widgets = {
            'validity': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
