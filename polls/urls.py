from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about.html/', views.about, name="about"),
    path('post.html/', views.post, name="post"),
    path('contact.html/', views.contact, name="contact"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
