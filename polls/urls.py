from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about.html/', views.about, name="about"),
    path('post.html/', views.post, name="post"),
    path('sign_up.html/', views.signup, name="sign_up"),
    path('sign_in.html/', views.sign_in, name="sign_in"),
    path('sign_out/', views.logout_view, name="sign_out"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
