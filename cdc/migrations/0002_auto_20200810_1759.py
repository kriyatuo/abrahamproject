# Generated by Django 3.0.8 on 2020-08-10 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personne',
            old_name='Type_personne',
            new_name='type_personne',
        ),
        migrations.RenameField(
            model_name='recuperation',
            old_name='medicaments',
            new_name='medicament',
        ),
    ]