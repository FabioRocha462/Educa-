from django.db import models
import uuid

from apps.users.models import User
from apps.products.models import Food
# Create your models here.
class Event(models.Model):
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
    uuid = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    school = models.CharField(max_length=2, choices=choices)
    date = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    status_activated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

#relations food and event with date and quantity attributes

class Food_Event(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
