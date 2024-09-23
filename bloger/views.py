from django.shortcuts import render

def Homepage_view(request):
    return render(request,"Homepage.html")

def aboutpage_view(request):
    return render(request,"about.html")
