from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
# --------------------------------------------------------------------------------------------------------------------
from import_export import fields, resources
from reversion.admin import VersionAdmin
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
# --------------------------------------------------------------------------------------------------------------------
admin.site.site_header = 'DASHBOARD PHARMACIE'
admin.site.title = "Gestion du niveau de stock"


# ------------------------------------------------------------------------------------------------------------
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('code', 'nom_fournisseur')

# ------------------------------------------------------------------------------------------------------------


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
# ----------------------------------------------------------------------------------------------------------------


class PersonneResource(resources.ModelResource):
    class Meta:
        model = Personne
        import_id_fields = ('code',)
        exclude = ('id', )


@admin.register(Personne)
class PersonneAdmin(ImportExportModelAdmin, VersionAdmin):
    resource_class = PersonneResource
    list_display = ('type_personne', 'code', 'nom', 'prenom')
# -----------------------------------------------------------------------------------------------------------------


class LotResource(resources.ModelResource):
    class Meta:
        model = Lot
        import_id_fields = ('numero_lot',)
        exclude = ('id', )


@admin.register(Lot)
class LotAdmin(ImportExportModelAdmin, VersionAdmin):
    resource_class = LotResource
    list_display = ('Livraison', 'produit', 'numero_lot',
                    'unite', 'quantite_lot', 'date_de_peremption')
# ------------------------------------------------------------------------------------------------------------------


admin.site.register(Livraison, LivraisonAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Type_personne)
#admin.site.register(Personne, PersonneAdmin)
admin.site.register(Produit)
admin.site.register(Dispensation, DispensationAdmin)
#admin.site.register(Lot, LotAdmin)
admin.site.unregister(Group)
