from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def myposts(request):
    posts = request.user.contents.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(posts, 2)
    return render(request, 'pages/myposts.html',context= {
        'posts': paginator.get_page(page),

    })    