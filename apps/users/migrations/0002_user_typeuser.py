# Generated by Django 4.1.5 on 2023-01-26 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='typeUser',
            field=models.CharField(blank=True, choices=[('secretary', 'Secretary'), ('asg', 'Asg'), ('coordinator', 'Coordinator'), ('nutricionist', 'Nutricionist')], max_length=20, null=True),
        ),
    ]
