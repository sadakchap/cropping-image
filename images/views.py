from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def photo_list(request):
    photos = Photo.objects.all()
    form = PhotoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('photo_list')
    return render(request, 'images/photo_list.html', {'form': form, 'photos': photos})