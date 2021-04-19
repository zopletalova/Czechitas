from django.db import models

class Auto(models.Model):
  RZ = models.CharField(max_length=100)
  zn_typ = models.CharField(max_length=100)
  najeto_km = models.IntegerField()
  dat_technicke = models.DateField()

class Zakaznik(models.Model):
  jmeno = models.CharField(max_length=100)
  prijmeni = models.CharField(max_length=100)
  RP_cislo = models.CharField(max_length=20)
  dat_narozeni = models.DateField()

class Vypujcka(models.Model):
  vypujceno = models.DateTimeField()
  vraceno = models.DateTimeField()
  cena = models.IntegerField()
