from django.urls import path

from pets import views

urlpatterns = [
    path('pets/', views.pet_all, name='pet_all'),
    path('pets/details/<int:pk>/', views.pet_detail, name='pet-detail')

]
