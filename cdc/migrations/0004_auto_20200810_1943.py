# Generated by Django 3.0.8 on 2020-08-10 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdc', '0003_auto_20200810_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type_personne',
            name='description',
            field=models.TextField(blank=True, help_text='description du type de personne'),
        ),
    ]
