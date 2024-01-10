from django.contrib import admin
from .models import Diary, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Diary)