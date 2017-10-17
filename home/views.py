from django.shortcuts import render

from .models import App

# Create your views here.
def landing(request):
    apps = App.objects.all()
    context = { 'apps': apps }
    return render(request, 'home/index.html', context)