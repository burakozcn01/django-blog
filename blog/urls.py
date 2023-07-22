from django.urls import path
from blog.views import contact , home
 
urlpatterns = [
    path('', home),
    path('contact/', contact),
]
