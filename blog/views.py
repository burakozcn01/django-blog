from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import PostModel, CategoryModel

def home(request):
    query = request.GET.get('q')
    posts = PostModel.objects.order_by('-created_date')
    if query:
        posts = PostModel.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(posts, 2) 
    posts = paginator.get_page(page)
    return render(request, 'pages/index.html', {'posts': posts})

def postdetail(request, slug):
    post = get_object_or_404(PostModel, slug=slug)
    comments = post.comments.all()
    return render(request, 'pages/postdetail.html', context={
        'post': post,
        'comments': comments
    })

def posts(request):
    posts = PostModel.objects.order_by('-created_date')
    page = request.GET.get('page')
    paginator = Paginator(posts, 2)
    return render(request, 'pages/posts.html', context={
        'posts': paginator.get_page(page),
    })

def contact(request):
    context = {
        'title': 'İletişim',
        'heading': 'Bizimle İletişime Geçin',
    }
    return render(request, 'pages/contact.html', context=context)

def category(request, categorySlug):
    category = get_object_or_404(CategoryModel, slug=categorySlug)
    posts = PostModel.objects.filter(category=category).order_by('-created_date')
    page = request.GET.get('page')
    paginator = Paginator(posts, 2)
    posts = paginator.get_page(page)
    return render(request, 'pages/category.html', context={
        'posts': posts,
        'category_name': category.name
    })
