from django.shortcuts import render, get_object_or_404
from blog.models import PostModel 


def postdetail(request, slug):
    post = get_object_or_404(PostModel , slug=slug)
    comments = post.comments.all()
    return render(request, 'pages/postdetail.html', context = {
        'post': post, 
        'comments': comments})