# Generated by Django 2.2 on 2020-02-14 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20200214_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]