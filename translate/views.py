from django.shortcuts import render
from .models import Word

def home(request):
    data = Word.objects.all()
    return render(request, 'translate/home.html', {'data': data})
