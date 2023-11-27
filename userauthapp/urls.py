from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login_view,name='login'),
    path('create/', views.create,name='create'),
    path('dashboard/', views.dashboard,name='dashboard'),
]