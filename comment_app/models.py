from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from PIL import image
from tkinter import image
# Create your models here.

class Post(models.Model):
    image = models.imageField(
        default ="default_foo.png", upload_to ="post_picture")
    caption = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey (User, on_delete = models.CASCADE)

    def __str__(self):
        return  f'{self.author.username}\'s Post-{self.title}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img= image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Comment:
    pass

    

