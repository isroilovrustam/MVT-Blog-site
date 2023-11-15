from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
]