from django.shortcuts import render

def home(request):
    data = {'window':'fenetre', 'door':'porte'}
    return render(request, 'translate/home.html', {'data': data})
