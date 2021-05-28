from django.conf.urls.i18n import i18n_patterns
from django.urls import path

from .views import *

app_name = 'deneyap'
urlpatterns = [
    path('', Main, name='main-page'),
    path('Teknoloji-Atolyesi/', TeknolojiAtolyesi, name='TeknolojiAtolyesi-page'),
    path('Turkiye-Teknoloji-Takımı-Vakfı/', TurkiyeTeknolojiTakımıVakfı, name='TurkiyeTeknolojiTakımıVakfı-page'),
    path('Kurumsal-Kimlik/', KurumsalKimlik, name='KurumsalKimlik-page'),
    path('Atolyelerimiz/', Atolyelerimiz, name='Atolyelerimiz-page'),
    path('Egitim-Amacı/', EgitimAmaci, name='EgitimAmaci-page'),
    path('Galerimiz/', Galerimiz, name='Galerimiz'),
    path('Atolyelerimiz-Detay/', AtolyelerimizDetay, name='Atolyelerimiz-Detay'),
    path('Egitim-Baslikleri/', EgitimBaslikleri, name='Egitim-Baslikleri'),
    path('Egitim-Baslikleri-Detay/', EgitimBaslikleriDetay, name='Egitim-Baslikleri-Detay'),
    path('Egitim-Sureci/', EgitimSureci, name='Egitim-Sureci'),
    path('Galerimiz-Detay/', GalerimizDetay, name='Galerimiz-Detay'),
    path('Iletisim/', Iletisim, name='Iletisim'),
]
