from django.db import models
import uuid
from apps.users.models import User
# Create your models here.

class Memorando(models.Model):
    choicesSecretary = (
        ('Secretaria de Planejamento','Secretaria de Planejamento'),
        ('Secretaria de Obras','Secretaria de Obras'),
        ('Secretaria de Finanças','Secretaria de Finanças'),
        ('Gabinete do Prefeito','Gabinete do Prefeito'),
        ('Camâra de Vereadores','Camâra de Vereadores'),
        ('Secretaria de Educação','Secretaria de Educação'),
        ('Outros','Outros'),
    )
    uuid = models.UUIDField(primary_key = True,unique = True, editable = False, default=uuid.uuid4)
    others = models.CharField(max_length = 255, null=True, blank=True)
    number = models.IntegerField()
    receiver = models.CharField(max_length=255,null=True, blank=True)
    title =  models.CharField(max_length = 10000, null=True, blank = True)
    destiny = models.CharField(max_length=50, choices=choicesSecretary)
    confirm = models.BooleanField(default=False, null = True, blank = True)
    description = models.TextField(null=True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.number) + "/" + str(self.created_at)

class Official(models.Model):
    choicesSecretary = (
        ('Secretaria de Planejamento','Secretaria de Planejamento'),
        ('Secretaria de Obras','Secretaria de Obras'),
        ('Secretaria de Finanças','Secretaria de Finanças'),
        ('Gabinete do Prefeito','Gabinete do Prefeito'),
        ('Camâra de Vereadores','Camâra de Vereadores'),
        ('Secretaria de Educação','Secretaria de Educação'),
        ('Outros','Outros'),
    )
    uuid = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)
    number = models.IntegerField()
    others = models.CharField(max_length=255, null=True, blank=True)
    title =  models.CharField(max_length = 10000, null=True, blank = True)
    receiver = models.CharField(max_length=255,null=True, blank=True)
    destiny = models.CharField(max_length=50, choices=choicesSecretary)
    confirm = models.BooleanField(default=False, null = True, blank = True)
    description = models.TextField(null=True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.number) + "/" + str(self.created_at) 


class Requeriment(models.Model):
    choicesSecretary = (
        ('Secretaria de Planejamento','Secretaria de Planejamento'),
        ('Secretaria de Obras','Secretaria de Obras'),
        ('Secretaria de Finanças','Secretaria de Finanças'),
        ('Gabinete do Prefeito','Gabinete do Prefeito'),
        ('Camâra de Vereadores','Camâra de Vereadores'),
        ('Secretaria de Educação','Secretaria de Educação'),
        ('Outros','Outros'),
    )
    uuid = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)
    number = models.IntegerField()
    title =  models.CharField(max_length = 10000, null=True, blank = True)
    others = models.CharField(max_length=255, null=True, blank=True)
    receiver = models.CharField(max_length=255,null=True, blank=True)
    destiny = models.CharField(max_length=50, choices=choicesSecretary)
    confirm = models.BooleanField(default=False, null = True, blank = True)
    description = models.TextField(null=True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.number) + "/" + str(self.created_at) 