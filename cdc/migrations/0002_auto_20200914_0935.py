# Generated by Django 3.0.8 on 2020-09-14 09:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cdc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispensation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date de dispensation')),
                ('quantite', models.IntegerField(verbose_name='Quantité recuperée')),
                ('next_rdv', models.DateField(verbose_name='date de prochain de rdv')),
                ('qte_next_rdv', models.IntegerField(verbose_name='Quantité à recuperer au prochain rdv')),
            ],
            options={
                'verbose_name': 'Dispensation',
                'verbose_name_plural': 'Dispensations',
            },
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_lot', models.CharField(blank=True, max_length=25, verbose_name='numero de lot')),
                ('unite', models.CharField(max_length=50, verbose_name="l'unité du lot")),
                ('quantite_lot', models.IntegerField(verbose_name='quantite du lot')),
                ('date_de_peremption', models.DateField()),
                ('Livraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lot', to='cdc.Livraison')),
            ],
            options={
                'verbose_name': 'Lot',
                'verbose_name_plural': 'Lots',
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_produit', models.CharField(blank=True, max_length=30, verbose_name='Designation du Produit')),
                ('unite', models.CharField(blank=True, max_length=30, verbose_name='unité du Produit')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
            },
        ),
        migrations.RemoveField(
            model_name='recuperation',
            name='medicament',
        ),
        migrations.RemoveField(
            model_name='recuperation',
            name='personne',
        ),
        migrations.AddField(
            model_name='personne',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personne',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='personne',
            name='nom',
            field=models.TextField(blank=True, max_length=40, verbose_name='nom de la personne'),
        ),
        migrations.AlterField(
            model_name='personne',
            name='prenom',
            field=models.TextField(blank=True, max_length=50, verbose_name='prenom de la personne'),
        ),
        migrations.DeleteModel(
            name='Batch',
        ),
        migrations.DeleteModel(
            name='Medicament',
        ),
        migrations.DeleteModel(
            name='Recuperation',
        ),
        migrations.AddField(
            model_name='lot',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lot', to='cdc.Produit'),
        ),
        migrations.AddField(
            model_name='dispensation',
            name='personne',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dispensation', to='cdc.Personne'),
        ),
        migrations.AddField(
            model_name='dispensation',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dispensation', to='cdc.Produit'),
        ),
    ]
