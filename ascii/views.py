from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ImageUploadForm

# Create your views here.

def upload_view(request):

    form = ImageUploadForm
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse('upload_form'))
        else:
            form = ImageUploadForm()
    return render(request, 'home.html', {'form': form})
    
