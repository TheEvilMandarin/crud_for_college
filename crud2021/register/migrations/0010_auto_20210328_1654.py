# Generated by Django 3.1.6 on 2021-03-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_auto_20210206_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prepod',
            name='sex',
            field=models.CharField(choices=[('ч', 'чол'), ('ж', 'жін')], default='ч', max_length=1),
        ),
        migrations.AlterField(
            model_name='spisok_stud',
            name='sex',
            field=models.CharField(choices=[('ч', 'чол'), ('ж', 'жін')], default='ч', max_length=1),
        ),
    ]
