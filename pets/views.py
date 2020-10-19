from django.shortcuts import render, redirect

# Create your views here.
from pets.forms import PetCreateForm
from pets.models import Pet, Like


def pet_all(request):
    context = {
        'pet': Pet.objects.all()
    }
    return render(request, 'pets/pet_list.html', context)


def pet_detail(request, pk):
    context = {
        'pet': Pet.objects.get(pk=pk)
    }
    return render(request, 'pets/pet_detail.html', context)


def pets_like(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like.objects.get(pet=pet)
    like.pet = pet
    like.save()

    return redirect('pets/pet_detail.html', pk)


def create_pet(request):
    if request.method == 'POST':
        pass
    context = {
        'form': PetCreateForm()
    }
    return render(request, 'pets/pet_create.html', context)


def edit_pet(request, pk):
    pass


def delete_pet(request, pk):
    pass
