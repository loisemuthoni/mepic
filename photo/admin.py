from django.contrib import admin
from .models import Images, Category, Location

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "pub_date", "location", "category"]
    class Meta:
        model = Images

admin.site.register(Images, ImageAdmin )
admin.site.register(Category)
admin.site.register(Location)
