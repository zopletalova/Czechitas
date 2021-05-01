from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView
from . import models

class VypujckyPrehledView(ListView):
    model = models.Vypujcka
    template_name = "vypujcky/vypujcky_list.html"

class IndexView(View):
    def get(self, request):
        return HttpResponse("<h1 align='center'><font color='fuchsia'> Vítejte v naší autopůjčovně!</font></h1>"
                            "<p align='center'>"
                            "<a href='http://localhost:8000/katalog/autazak/'>Jaká auta máme?</a><br>"
                            "</p>"
                            "<h2 align='center'>O naší autopůjčovně</h2>"
                            "<p align='center'>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>"
                            "<h2 align='center'><font color='blue'>Nabízíme následující auta:</font></h2>"
                            "<br/>"
                            "<ul align=='left'>"
                                "<li>Nákladní</li>"
                                "<li>Osobní</li>"
                                "<li>Dodávky</li>"
                            "</ul>")

class SeznamAutView(ListView):
    model = models.Auto
    template_name = "auta/auta_list.html"

class SeznamAutProZakView(ListView):
    model = models.Auto
    template_name = "auta/autazak_list.html"


class SeznamZakaznikuView(ListView):
    model = models.Zakaznik
    template_name = "zakaznici/zakaznici_list.html"
