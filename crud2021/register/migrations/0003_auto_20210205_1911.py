# Generated by Django 3.1.5 on 2021-02-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_specialnost_n_specialnosty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialnost',
            name='n_specialnosty',
            field=models.CharField(max_length=5),
        ),
    ]
