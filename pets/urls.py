from django.urls import path

from pets import views

urlpatterns = [
    path('', views.pet_all, name='pet_all'),
    path('details/<int:pk>/', views.pet_detail, name='pet-detail'),
    path('like/<int:pk>/', views.pets_like, name='pets-like')

]
