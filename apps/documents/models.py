from django.db import models
import uuid
from apps.account.models import User
# Create your models here.

class Memorando(models.Model):
    choicesSecretary = (
        ('1','Secretaria de Planejamento'),
        ('2','Secretaria de Obras'),
        ('3','Secretaria de Finanças'),
        ('4','Gabinete do Prefeito'),
        ('5','Camâra de Vereadores'),
        ('6','Secretaria de Educação'),
        ('7','Outros'),
    )
    uuid = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)
    others = models.CharField(max_length=255, null=True, blank=True)
    number = models.IntegerField()
    receiver = models.CharField(max_length=255,null=True, blank=True)
    destiny = models.CharField(max_length=2, choices=choicesSecretary)
    description = models.TextField(null=True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.number) + "/" + str(self.created_at)

class Official(models.Model):
    choicesSecretary = (
        ('1','Secretaria de Planejamento'),
        ('2','Secretaria de Obras'),
        ('3','Secretaria de Finanças'),
        ('4','Gabinete do Prefeito'),
        ('5','Camâra de Vereadores'),
        ('6','Secretaria de Educação'),
        ('7','Outros'),
    )
    uuid = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)
    number = models.IntegerField()
    others = models.CharField(max_length=255, null=True, blank=True)
    receiver = models.CharField(max_length=255,null=True, blank=True)
    destiny = models.CharField(max_length=2, choices=choicesSecretary)
    description = models.TextField(null=True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.number) + "/" + str(self.created_at) 


class Requeriment(models.Model):
    choicesSecretary = (
        ('1','Secretaria de Planejamento'),
        ('2','Secretaria de Obras'),
        ('3','Secretaria de Finanças'),
        ('4','Gabinete do Prefeito'),
        ('5','Camâra de Vereadores'),
        ('6','Secretaria de Educação'),
        ('7','Outros'),
    )
    uuid = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)
    number = models.IntegerField()
    others = models.CharField(max_length=255, null=True, blank=True)
    receiver = models.CharField(max_length=255,null=True, blank=True)
    destiny = models.CharField(max_length=2, choices=choicesSecretary)
    description = models.TextField(null=True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.number) + "/" + str(self.created_at) 