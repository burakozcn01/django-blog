from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    context = {
        'title': 'naber cano',
        'heading': 'maraba cano',
    }
    return render(request, 'pages/contact.html', context=context)