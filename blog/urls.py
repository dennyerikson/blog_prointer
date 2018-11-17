from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('sobre/', views.sobre, name='sobre'),
    path('disp_moveis/', views.disp_moveis, name='disp_moveis')
]