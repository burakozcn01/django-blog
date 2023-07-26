from django.urls import path
from blog.views import contact , home, category, myposts

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('myposts', myposts, name='myposts'),
    
    ]
