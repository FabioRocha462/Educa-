# Generated by Django 4.1.5 on 2023-02-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_memorando_confirm_official_confirm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='memorando',
            name='title',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='official',
            name='title',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='requeriment',
            name='title',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
