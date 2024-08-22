from django.db import models

# Create your models here.

class MiseAJour(models.Model):
    TYPE_LOGICIEL_CHOICES =[
        ('Brel-Eco', 'Brel-Eco'),
        ('Brel-Gest', 'Brel-Gest'),
    ]
    date = models.DateField()
    version_Logiciel = models.CharField(max_length=50)
    type_logiciel = models.CharField(max_length=10, choices=TYPE_LOGICIEL_CHOICES)
    client = models.CharField(max_length=100)
    poste_concerne = models.CharField(max_length=100)
    addresse_MAC = models.CharField(max_length=17)
    agent = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.date}---{self.version_Logiciel}---{self.type_logiciel}---{self.poste_concerne}---{self.addresse_MAC}---{self.agent}---{self.client}"