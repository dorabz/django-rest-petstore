from django.contrib import admin

# Register your models here.
from api.models import Pet, Tag, Category

admin.site.register(Pet)
admin.site.register(Tag)
admin.site.register(Category)