from django.db import models
from apps.account.models import User
import uuid
# Create your models here.

class Food(models.Model):
    choices = (
        ("1","INOMPP"),
        ("2","Frutas e Polpas de Frutas"),
        ("3","Verduras/Legumes/Raízes"),
        ("4","INOMPNP"),
        ("5","Processados"),
        ("6","Ultraprocessados"),
        ("7","Ingredientes Culinários")
    )
    uuid = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4) 
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    validity = models.DateField()
    typeCategoria = models.CharField(
        max_length=1,
        choices= choices
    )
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
    food = models.ManyToManyField(Food)
    quantity = models.FloatField()
    status_activate = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user + " " + str(self.created_at)

class Request_Cleaning(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)
    cleaning = models.ManyToManyField(Cleaning)
    quantity = models.FloatField()
    status_activate = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user + " " + str(self.created_at)