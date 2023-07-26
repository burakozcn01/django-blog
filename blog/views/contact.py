from django.shortcuts import render

def contact(request):
    context = {
        'title': 'naber cano',
        'heading': 'maraba cano',
    }
    return render(request, 'pages/contact.html', context=context)