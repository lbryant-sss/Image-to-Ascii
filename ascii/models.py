from django.db import models

# Create your models here.

class ImageUpload(models.Model):
    my_image = models.ImageField(upload_to='image-uploads/')
    created_on = models.DateField(auto_now_add=True)



