from django.urls import path

from app1.views import CustomUserFormView, CustomUserLoginView, IndexView, HomeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register', CustomUserFormView.as_view(), name='register'),
    path('login', CustomUserLoginView.as_view(), name='login'),
    path('home', HomeView.as_view(), name='home')
]
