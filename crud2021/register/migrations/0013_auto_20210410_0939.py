# Generated by Django 3.1.6 on 2021-04-10 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_auto_20210328_2345'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='predmety',
            unique_together={('nazv_predmeta', 'specialnost')},
        ),
    ]
