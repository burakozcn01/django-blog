from django.urls import path
from blog.views import contact , home, category, myposts, postdetail

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('myposts', myposts, name='myposts'),
    path('postdetail/<slug:slug>', postdetail, name='postdetail'),

    
    ]
