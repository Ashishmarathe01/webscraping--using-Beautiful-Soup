# Generated by Django 3.2.3 on 2021-05-18 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Swords', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='words',
            name='url',
        ),
    ]
