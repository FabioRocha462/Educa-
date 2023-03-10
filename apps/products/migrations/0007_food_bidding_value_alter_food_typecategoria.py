# Generated by Django 4.1.5 on 2023-02-11 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_request_cleaning_cleaning_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='bidding_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='typeCategoria',
            field=models.CharField(choices=[('INOMPP', 'INOMPP'), ('Frutas e Polpas de Frutas', 'Frutas e Polpas de Frutas'), ('Verduras/Legumes/Raízes', 'Verduras/Legumes/Raízes'), ('INOMPNP', 'INOMPNP'), ('Processados', 'Processados'), ('Ultraprocessados', 'Ultraprocessados'), ('Ingredientes Culinários', 'Ingredientes Culinários')], max_length=50),
        ),
    ]
