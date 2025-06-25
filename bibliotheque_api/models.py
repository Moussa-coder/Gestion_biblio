from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

def default_date_retour():
    return timezone.now() + timedelta(days=14)

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=200)
    image = models.ImageField(upload_to='livres/', null=True, blank=True)
    disponible = models.BooleanField(default=True)  # type: ignore

    def __str__(self):
        return f"{self.titre} - {self.auteur}"


class Emprunt(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_emprunt = models.DateField(default=timezone.now)
    date_retour = models.DateField(default=default_date_retour)
    rendu = models.BooleanField(default=False)  # type: ignore
    en_retard = models.BooleanField(default=False)  # type: ignore

    def __str__(self):
        return f"{self.utilisateur.username} - {self.livre.titre}"  # type: ignore

class ProfilUtilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departement = models.CharField(max_length=100)
    filiere = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username  # type: ignore
