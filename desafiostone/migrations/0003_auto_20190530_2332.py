# Generated by Django 2.2.1 on 2019-05-31 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafiostone', '0002_auto_20190530_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='idade',
            field=models.IntegerField(default=0),
        ),
    ]
