from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup', views.signup, name = 'signup'),
    path('upload',views.upload, name='upload'),
    path('login', views.login, name='login'),
    path('logout',views.logout, name='logout')
]