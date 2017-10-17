from django.shortcuts import render

def coming_soon(request):
    return render(request, 'home/coming_soon.html')