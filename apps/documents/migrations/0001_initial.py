# Generated by Django 4.1.5 on 2023-01-15 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Requeriment',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('number', models.IntegerField()),
                ('others', models.CharField(blank=True, max_length=255, null=True)),
                ('receiver', models.CharField(blank=True, max_length=255, null=True)),
                ('destiny', models.CharField(choices=[('1', 'Secretaria de Planejamento'), ('2', 'Secretaria de Obras'), ('3', 'Secretaria de Finanças'), ('4', 'Gabinete do Prefeito'), ('5', 'Camâra de Vereadores'), ('6', 'Secretaria de Educação'), ('7', 'Outros')], max_length=2)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Official',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('number', models.IntegerField()),
                ('others', models.CharField(blank=True, max_length=255, null=True)),
                ('receiver', models.CharField(blank=True, max_length=255, null=True)),
                ('destiny', models.CharField(choices=[('1', 'Secretaria de Planejamento'), ('2', 'Secretaria de Obras'), ('3', 'Secretaria de Finanças'), ('4', 'Gabinete do Prefeito'), ('5', 'Camâra de Vereadores'), ('6', 'Secretaria de Educação'), ('7', 'Outros')], max_length=2)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Memorando',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('others', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.IntegerField()),
                ('receiver', models.CharField(blank=True, max_length=255, null=True)),
                ('destiny', models.CharField(choices=[('1', 'Secretaria de Planejamento'), ('2', 'Secretaria de Obras'), ('3', 'Secretaria de Finanças'), ('4', 'Gabinete do Prefeito'), ('5', 'Camâra de Vereadores'), ('6', 'Secretaria de Educação'), ('7', 'Outros')], max_length=2)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
