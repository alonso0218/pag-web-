from django.shortcuts import render

# Create your views here.
def reservas(requets):
    return render(requets,"reservasapp/reservas.html")