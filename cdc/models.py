from django.db import models
from django.db.models import Sum


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


class Personne(models.Model):
    type_personne = models.ForeignKey(
        'Type_personne',
        on_delete=models.CASCADE, related_name="personnes",
        verbose_name='la personne qui récupère les médicaments'
    )
    code = models.CharField(verbose_name='code personne', max_length=25)
    nom = models.CharField(
        verbose_name='nom de la personne', max_length=40, blank=True)
    prenom = models.CharField(
        verbose_name='prenom de la personne', max_length=50, blank=True)

    def __str__(self):
        return '{} - {} {}'.format(self.type_personne, self.nom, self.prenom)

    class Meta:
        verbose_name = 'Personne'
        verbose_name_plural = 'Personnes'


class Produit(models.Model):
    nom_produit = models.CharField(
        verbose_name='nom du Produit', max_length=30, blank=True)
    alerte = models.IntegerField(
        verbose_name='seuil à ne pas franchir', blank=True)

    @property
    def quantite_disponible(self):
        return self.lot.all().aggregate(qte=Sum('quantite_batch'))['qte'] - self.dispensation.all().aggregate(qte=Sum('quantite'))['qte']
    """
    @property
    def signale(self):
        while self.alerte > self.quantite_disponible:
            print("attention stock ")
    """

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
    date = models.DateField()
    quantite = models.IntegerField(
        verbose_name='Quantité recuperée')

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
    quantite_lot = models.IntegerField(verbose_name='quantite du lot')

    def __str__(self):
        return '{}, {}, {}'.format(self.numero_lot, self.produit, self.quantite_lot)

    class Meta:
        verbose_name = 'Lot'
        verbose_name_plural = 'Lots'
