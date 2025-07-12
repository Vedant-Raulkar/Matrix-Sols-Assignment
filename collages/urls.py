from django.urls import path
from . import views

app_name = 'collages'

urlpatterns = [
    path('', views.home, name='home'),
    path('collages/', views.collage_list, name='list'),
    path('collages/create/', views.collage_create, name='create'),
    path('collages/<int:pk>/', views.collage_detail, name='detail'),
    path('collages/<int:pk>/delete/', views.collage_delete, name='delete'),
]
