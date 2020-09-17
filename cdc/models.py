from django.db import models
from django.db.models import Sum

# -------------------------------------------------------------------------------------------------------------------
# Create your models here.


class MonitoredTimeModel(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
# ------------------------------------------------------------------------------------------------------------------


class Fournisseur(models.Model):
    code = models.CharField(
        verbose_name='le code du fournisseur', max_length=25)
    nom_fournisseur = models.CharField(
        verbose_name="le nom de l'organisme fournisseur", max_length=100, blank=False)

    def __str__(self):
        return self.nom_fournisseur

    class Meta:
        verbose_name = 'Fournisseur'
        verbose_name_plural = 'Fournisseurs'


class Type_personne(models.Model):
    libelle = models.CharField(
        verbose_name='la personne qui récupère les médicaments', max_length=70, blank=False)
    description = models.TextField(
        help_text='description du type de personne', blank=True)

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name = 'Type de personne'
        verbose_name_plural = 'Type de personnes'


class Livraison(models.Model):
    fournisseur = models.ForeignKey(
        'fournisseur',
        on_delete=models.CASCADE,
        verbose_name='le fournisseur de la livraison', related_name="livraisons", blank=False
    )
    date = models.DateField(verbose_name='date de livraison')

    def __str__(self):
        return '{}, {}'.format(self.fournisseur, self.date)

    class Meta:
        verbose_name = 'Livraision'
        verbose_name_plural = 'Livraisons'


class Personne(MonitoredTimeModel):
    type_personne = models.ForeignKey(
        'Type_personne',
        on_delete=models.CASCADE, related_name="personnes",
        verbose_name='la personne qui récupère les médicaments'
    )
    code = models.CharField(verbose_name='code personne', max_length=25)
    nom = models.TextField(
        verbose_name='nom de la personne', max_length=40, blank=True)
    prenom = models.TextField(
        verbose_name='prenom de la personne', max_length=50, blank=True)

    @property
    def derniere_visite(self):
        return self.dispensation.latest('creation_time')

    def __str__(self):
        return '{} - {} {}'.format(self.type_personne, self.nom, self.prenom)

    class Meta:
        verbose_name = 'Personne'
        verbose_name_plural = 'Personnes'


class Produit(models.Model):
    designation_produit = models.CharField(
        verbose_name='Designation du Produit', max_length=30, blank=True)
    unite = models.CharField(
        verbose_name='unité du Produit', max_length=30, blank=True)
    alerte = models.IntegerField(
        verbose_name='seuil à ne pas franchir', blank=True)

    @property
    def quantite_disponible(self):
        return self.lot.all().aggregate(qte=Sum('quantite_lot'))['qte'] - self.dispensation.all().aggregate(qte=Sum('quantite'))['qte']

    @property
    def alerte(self):
        if self.quantite_disponible <= 500:
            def send(self, messages):
                " STOCK inférieur à 500. Bientôt en manque "

    def __str__(self):
        return '{} : {}'.format(self.nom_produit, self.quantite_disponible)

    class Meta:
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'


class Dispensation(models.Model):
    personne = models.ForeignKey(
        'Personne',
        on_delete=models.CASCADE, related_name="dispensation"
    )
    produit = models.ForeignKey(
        'Produit',
        on_delete=models.CASCADE, related_name="dispensation"
    )
    date = models.DateField(verbose_name="date de dispensation", )
    quantite = models.IntegerField(
        verbose_name='Quantité recuperée')
    next_rdv = models.DateField(verbose_name="date de prochain de rdv", )
    qte_next_rdv = models.IntegerField(
        verbose_name='Quantité à recuperer au prochain rdv')

    def __str__(self):
        return '{} ({} x {}) {}'.format(self.personne, self.quantite, self.produit, self.date)

    class Meta:
        verbose_name = 'Dispensation'
        verbose_name_plural = 'Dispensations'


class Lot(models.Model):
    Livraison = models.ForeignKey(
        'Livraison',
        on_delete=models.CASCADE, related_name="lot",
    )
    produit = models.ForeignKey(
        'Produit',
        on_delete=models.CASCADE, related_name="lot",
    )
    numero_lot = models.CharField(
        verbose_name='numero de lot', max_length=25, blank=True)
    unite = models.CharField(verbose_name="l'unité du lot", max_length=50)
    quantite_lot = models.IntegerField(verbose_name='quantite du lot')
    date_de_peremption = models.DateField()

    def __str__(self):
        return '{}, {}, {}'.format(self.numero_lot, self.produit, self.quantite_lot)

    class Meta:
        verbose_name = 'Lot'
        verbose_name_plural = 'Lots'
