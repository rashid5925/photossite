from django.shortcuts import render

def babies(request):
    return render(request, 'babies.html')

def products(request):
    return render(request, 'products.html')

def landscape(request):
    return render(request, 'landscape.html')
