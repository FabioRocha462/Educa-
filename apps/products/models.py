from django.db import models
from apps.users.models import User
import uuid
# Create your models here.

class Food(models.Model):
    choices = (
        ("INOMPP","INOMPP"),
        ("Frutas e Polpas de Frutas","Frutas e Polpas de Frutas"),
        ("Verduras/Legumes/Raízes","Verduras/Legumes/Raízes"),
        ("INOMPNP","INOMPNP"),
        ("Processados","Processados"),
        ("Ultraprocessados","Ultraprocessados"),
        ("Ingredientes Culinários","Ingredientes Culinários")
    )
    uuid = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4) 
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    validity = models.DateField()
    typeCategoria = models.CharField(
        max_length=50,
        choices= choices
    )
    bidding_value = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Cleaning(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Request_Food(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, null=True, blank=True)
    status_activate = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    

    def __str__(self):
        return self.name

class Food_RequestFood(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    requestfood = models.ForeignKey(Request_Food, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)

class Request_Cleaning(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, null=True, blank=True)
    status_activate = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Cleaning_RequestCleaning(models.Model):
    cleaning = models.ForeignKey(Cleaning, on_delete=models.CASCADE, null=True, blank=True)
    requestcleaning =  models.ForeignKey(Request_Cleaning, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)