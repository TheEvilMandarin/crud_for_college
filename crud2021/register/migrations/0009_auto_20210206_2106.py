# Generated by Django 3.1.5 on 2021-02-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_merge_20210206_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spisok_stud',
            name='sex',
            field=models.CharField(choices=[('м', 'муж'), ('ж', 'жен')], default='м', max_length=1),
        ),
    ]
