from django.db import models


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField(upload_to='blog/')
    body = models.TextField()
    tag = models.ManyToManyField(Tag, )

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    full_name = models.CharField(max_length=202)
    phone = models.CharField(max_length=202)
    email = models.EmailField()
    message = models.TextField()

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
