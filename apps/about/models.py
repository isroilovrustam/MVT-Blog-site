from django.db import models


# Create your models here.

class About(models.Model):
    full_name = models.CharField(max_length=202)
    job = models.CharField(max_length=202)
    image = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=202)
    description = models.TextField()
    twitter = models.CharField(max_length=202)
    facebook = models.CharField(max_length=202)
    instagram = models.CharField(max_length=202)

    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
