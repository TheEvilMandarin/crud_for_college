# Generated by Django 3.1.5 on 2021-02-05 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialnost',
            name='n_specialnosty',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
