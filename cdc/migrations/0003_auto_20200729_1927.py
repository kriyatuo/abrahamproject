# Generated by Django 3.0.8 on 2020-07-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdc', '0002_auto_20200729_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='batch',
            name='font_size',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='font_size',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livraison',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livraison',
            name='font_size',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicaments',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicaments',
            name='font_size',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personnes',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personnes',
            name='font_size',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuperation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuperation',
            name='font_size',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='type_personne',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='type_personne',
            name='font_size',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='batch',
            name='quantite',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='recuperation',
            name='quantite',
            field=models.FloatField(max_length=10),
        ),
    ]