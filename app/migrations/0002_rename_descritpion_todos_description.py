# Generated by Django 4.0.2 on 2022-02-22 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todos',
            old_name='descritpion',
            new_name='description',
        ),
    ]
