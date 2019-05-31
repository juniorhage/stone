# Generated by Django 2.2.1 on 2019-05-31 00:17

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('idade', models.IntegerField(default=0)),
                ('cargo', models.CharField(max_length=255)),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
    ]
