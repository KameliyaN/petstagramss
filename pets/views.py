from django.shortcuts import render

# Create your views here.
from pets.models import Pet


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
