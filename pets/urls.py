from django.urls import path

from pets import views

urlpatterns = [
    path('', views.pet_all, name='pet_all'),
    path('details/<int:pk>/', views.pet_detail, name='pet-detail'),
    path('create/', views.create_pet, name='pet create'),
    path('like/<int:pk>/', views.pets_like, name='like pet'),
    path('edit/<int:pk>/', views.edit_pet, name='pet edit'),
    path('delete/<int:pk>/', views.delete_pet, name='pet delete'),

]
