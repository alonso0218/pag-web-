from django.shortcuts import render, HttpResponse

# Create your views here.
def autos (request):
    return render(request,"autosapp/autos.html")


