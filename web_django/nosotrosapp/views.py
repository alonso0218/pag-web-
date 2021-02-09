from django.shortcuts import render,HttpResponse

# Create your views here.

def nosotros (request):
    return render(request,"nosotrosapp/nosotros.html")
