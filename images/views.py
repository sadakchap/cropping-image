from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def photo_list(request):
    photos = Photo.objects.all()
    print(photos)
    if request.method == 'POST':
        form = PhotoForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'images/photo_list.html', {'form': form, 'photos': photos})