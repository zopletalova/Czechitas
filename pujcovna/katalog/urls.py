from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('auta/', views.SeznamAutView.as_view(), name='auta_list'),
    path('autazak/', views.SeznamAutProZakView.as_view(), name='autazak_list'),
    path('zakaznici/', views.SeznamZakaznikuView.as_view(), name='zakaznici_list'),
    path('vypujcky/', views.VypujckyPrehledView.as_view(), name='vypujcky_list'),
]
