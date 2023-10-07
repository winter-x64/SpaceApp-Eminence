from django.shortcuts import render

# Create your views here.
def landingpage(request):
    return render(request, "explore/landing_page.html")