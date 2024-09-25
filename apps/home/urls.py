from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('reports/',views.reports,name = 'reports'), # Xây dựng các function view tương ứng
    path('users/',views.users,name = 'users'), # Xây dựng các function view tương ứng
    path('reports/query/', views.query, name='query'),


]