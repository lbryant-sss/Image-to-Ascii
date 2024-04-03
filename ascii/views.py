from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ImageUploadForm
from .models import ImageUpload

# Create your views here.

def upload_view(request):

    form = ImageUploadForm
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            
            return redirect(reverse('images'))
        else:
            form = ImageUploadForm()
    return render(request, 'home.html', {'form': form})
    
def image_view(request):
    last_uploaded_image = ImageUpload.objects.last()
    return render(request, 'image.html', {'last_uploaded_image': last_uploaded_image})