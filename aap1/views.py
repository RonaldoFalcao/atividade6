from django.shortcuts import render

def home(request):
    nome = 'Ronaldo'
    sobrenome1 = 'Falcão'
    sobrenome2 = 'Filho'
    contexto = {
        'nome': nome,
        'sobrenome1': sobrenome1,
        'sobrenome2': sobrenome2
    }
    return render(request, 'home.html', contexto)
