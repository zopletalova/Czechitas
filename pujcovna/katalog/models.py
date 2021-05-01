from django.db import models
import datetime
import pytz

class Auto(models.Model):
  RZ = models.CharField(max_length=100)
  zn_typ = models.CharField(max_length=100)
  najeto_km = models.IntegerField()
  dat_technicke = models.DateField()

  @property
  def odtechnicke(self):
    dnes = datetime.datetime.now()
    dnes = pytz.UTC.localize(dnes)
    dnes = datetime.datetime.date(dnes)
    delka = dnes - self.dat_technicke
    return delka.days

class Zakaznik(models.Model):
  PROGRAM_DRUHY = (
    ('B', 'běžný zákazník'),
    ('Z', 'zlatý program'),
    ('P', 'platinový program'),
  )

  jmeno = models.CharField(max_length=100)
  prijmeni = models.CharField(max_length=100)
  RP_cislo = models.CharField(max_length=20)
  dat_narozeni = models.DateField()
  program = models.CharField(max_length=1, choices=PROGRAM_DRUHY, null=True)

class Vypujcka(models.Model):
  id_cislo = models.IntegerField()
  vypujceno = models.DateTimeField()
  vraceno = models.DateTimeField()
  cena = models.IntegerField()
  auto = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True)
  zakaznik = models.ForeignKey(Zakaznik, on_delete=models.SET_NULL, null=True)

  @property
  def urcistav(self):
    ted = datetime.datetime.now()
    ted = pytz.UTC.localize(ted)
    vypujceno = self.vypujceno
    vraceno = self.vypujceno
    if (ted >= vypujceno) & (ted <= vraceno):
      stav = "výpůjčka běží"
    elif ted > vraceno:
      stav = "výpůjčka skončila"
    elif ted < vypujceno:
      stav = "výpůjčka ještě nezačala"
    return stav