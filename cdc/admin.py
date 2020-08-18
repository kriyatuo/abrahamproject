from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.site_header = 'DASHBOARD PHARMACIE'
admin.site.title = "GESTION STOCK"


class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('code', 'nom_fournisseur')


class LivraisonAdmin(admin.ModelAdmin):
    list_display = ('fournisseur', 'date')
    list_filter = ('date',)


class PersonneAdmin(admin.ModelAdmin):
    list_display = ('type_personne', 'code', 'nom', 'prenom')


class DispensationAdmin(admin.ModelAdmin):
    list_display = ('date', 'personne', 'produit', 'quantite')
    list_filter = ('date',)


class LotAdmin(admin.ModelAdmin):
    list_display = ('numero_lot', 'produit', 'quantite_lot')


admin.site.register(Livraison, LivraisonAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Type_personne)
admin.site.register(Personne, PersonneAdmin)
admin.site.register(Produit)
admin.site.register(Dispensation, DispensationAdmin)
admin.site.register(Lot, LotAdmin)
admin.site.unregister(Group)
