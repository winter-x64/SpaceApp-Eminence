from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request, "welcome/welcomepage.html")


def home(request):
    return render(request, "home/homepage.html")


def aboutus(request):
    return render(request, "home/aboutuspage.html")


def contactus(request):
    return render(request, "home/contactuspage.html")
