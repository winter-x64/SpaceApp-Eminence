from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request, "welcome/welcome_page.html")


def aboutus(request):
    return render(request, "welcome/welcome_page.html")


def contactus(request):
    return render(request, "welcome/welcome_page.html")
