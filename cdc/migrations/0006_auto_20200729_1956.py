# Generated by Django 3.0.8 on 2020-07-29 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdc', '0005_auto_20200729_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='created',
        ),
        migrations.RemoveField(
            model_name='livraison',
            name='created',
        ),
        migrations.RemoveField(
            model_name='medicaments',
            name='created',
        ),
        migrations.RemoveField(
            model_name='personnes',
            name='created',
        ),
        migrations.RemoveField(
            model_name='recuperation',
            name='created',
        ),
        migrations.RemoveField(
            model_name='type_personne',
            name='created',
        ),
    ]