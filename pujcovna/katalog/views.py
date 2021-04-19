from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request):
        return HttpResponse("<h1 align='center'><font color='fuchsia'> Vítejte v naší autopůjčovně!</font></h1>"
                            "<p align='center'>"
                            "<a href='http://localhost:8000/katalog/seznam/'>Jaká auta máme?</a><br>"
                            "</p>"
                            "<h2 align='center'>O naší autopůjčovně</h2>"
                            "<p align='center'>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>"
                            "<h3 align='center'><font color='blue'>Nabízíme následující auta:</font></h2>"
                            "<br/>"
                            "<ul align=='left'>"
                                "<li>Nákladní</li>"
                                "<li>Osobní</li>"
                                "<li>Dodávky</li>"
                            "</ul>")
class SeznamView(View):
    def get(self, request):
        return HttpResponse('Zde bude seznam aut.')
