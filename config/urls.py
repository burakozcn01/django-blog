from django.contrib import admin
from django.urls import path    
from django.conf.urls.static import static
from django.conf import settings
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:categorySlug>/', views.category, name='category'),
    path('posts/', views.posts, name='posts'),
    path('post/<slug:slug>/', views.postdetail, name='postdetail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
