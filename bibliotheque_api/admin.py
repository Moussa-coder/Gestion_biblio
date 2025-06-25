from django.contrib import admin
from .models import Livre, Emprunt, ProfilUtilisateur

admin.site.register(Livre)
admin.site.register(Emprunt)
admin.site.register(ProfilUtilisateur)
