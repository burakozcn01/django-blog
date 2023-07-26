from django.shortcuts import render
from blog.models import PostModel
from django.core.paginator import Paginator
from django.db.models import Q

def home(request):
    query = request.GET.get('q')
    posts = PostModel.objects.order_by('-id')
    if query:
        posts = PostModel.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(posts, 2)
    posts = paginator.get_page(page)
    return render(request, 'pages/index.html', {'posts': posts})    