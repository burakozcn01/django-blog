from django.shortcuts import render ,get_object_or_404
from blog.models import PostModel , CategoryModel
from django.core.paginator import Paginator

def category(request, categorySlug):
    category = get_object_or_404(CategoryModel, slug=categorySlug)
    posts = PostModel.objects.filter(category=category).order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(posts, 2)
    posts = paginator.get_page(page)
    return render(request, 'pages/category.html',context= {
        'posts': paginator.get_page(page),
        'category_name': category.name

    })    