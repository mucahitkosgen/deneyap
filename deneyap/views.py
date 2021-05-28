from django.shortcuts import render


# Create your views here.
def Main(request):
    return render(request, "deneyap/index.html")


def TeknolojiAtolyesi(request):
    return render(request, "deneyap/deneyapteknolojiatolyesi.html")


def TurkiyeTeknolojiTakımıVakfı(request):
    return render(request, "deneyap/türkiyeteknolojitakimivakfi.html")


def KurumsalKimlik(request):
    return render(request, "deneyap/kurumsalkimlik.html")


def Atolyelerimiz(request):
    return render(request, "deneyap/atolyelerimiz.html")


def EgitimAmaci(request):
    return render(request, "deneyap/egitimamaci.html")


def Galerimiz(request):
    return render(request, "deneyap/galerimiz.html")


def AtolyelerimizDetay(request):
    return render(request, "deneyap/atolyelerimiz_detay.html")


def EgitimBaslikleri(request):
    return render(request, "deneyap/egitimbasliklari.html")


def EgitimBaslikleriDetay(request):
    return render(request, "deneyap/egitimbaslikleri_detay.html")


def EgitimSureci(request):
    return render(request, "deneyap/egitimsureci.html")


def GalerimizDetay(request):
    return render(request, "deneyap/galerimiz_detay.html")

def Iletisim(request):
    return render(request, "deneyap/iletisim.html")
