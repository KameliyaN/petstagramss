from django.http import HttpResponse
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
        form = PetCreateForm(request.POST)
        if form.is_valid():
            pet = form.save()
            pet.save()
            return redirect('pet_all')
        context = {
            'form': form
        }
        return render(request, 'pets/pet_create.html', context)

    context = {
        'form': PetCreateForm()
    }
    return render(request, 'pets/pet_create.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = PetCreateForm(request.POST, instance=pet)
        if form.is_valid():
            pet = form.save()
            pet.save()
            return redirect('pet-detail', pk=pk)
        return HttpResponse('not correct')
    context = {
        'form': PetCreateForm(instance=pet)
    }
    return render(request, 'pets/pet_edit.html', context)


def delete_pet(request, pk):
    pass
