from django.contrib import admin
from .models import Contact, Subscribe


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', "is_published")
    list_filter = ('create_date',)
    search_fields = ('full_name', 'phone')


admin.site.register(Subscribe)
