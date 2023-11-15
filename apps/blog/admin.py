from django.contrib import admin
from .models import Tag, Comment, Blog
# Register your models here.


admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Blog)
