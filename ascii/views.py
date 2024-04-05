from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ImageUploadForm
from .models import ImageUpload
from .converter import generate_ascii_art

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
    generate_ascii_art()
    ascii_image_url = '/media/ascii_images/generated_ascii_art.png'
    return render(request, 'image.html', {'last_uploaded_image': last_uploaded_image, 'ascii_image_url':ascii_image_url})