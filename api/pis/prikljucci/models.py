from django.db import models
from django.db.models.deletion import CASCADE

from korisnici.models import User
from prikljucak_statusi.models import StatusPrikljucka
from ulice.models import Ulica

class Prikljucak(models.Model):
    korisnik=models.ForeignKey(User, on_delete=CASCADE)
    ulica=models.ForeignKey(Ulica, on_delete=CASCADE)
    kucni_broj=models.IntegerField()
    samopopisivanje=models.BooleanField(default=False)
    date_created=models.DateField(auto_now_add=True)
    status=models.ForeignKey(StatusPrikljucka, on_delete=CASCADE)
    
    @property
    def get_ulica(self):
        return self.ulica.ulica

    @property
    def get_mjesto(self):
        return self.ulica.mjesto.mjesto
    
    @property
    def username(self):
        return self.korisnik.username
    
    @property
    def userlastname(self):
        return self.korisnik.userlastname
    
    
      

    