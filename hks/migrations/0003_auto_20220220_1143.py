# Generated by Django 3.2.12 on 2022-02-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hks', '0002_alter_vehicle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='Fuel_level',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='Temprature',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='average_speed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='speed',
            field=models.IntegerField(),
        ),
    ]