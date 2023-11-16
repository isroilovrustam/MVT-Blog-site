from django.contrib import admin
from .models import Tag, Comment, Blog


# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date')
    list_filter = ('create_date', )


admin.site.register(Tag)
admin.site.register(Comment)
