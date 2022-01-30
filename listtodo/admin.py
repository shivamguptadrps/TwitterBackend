from django.contrib import admin

from .models import Following,Users,Tweet

admin.site.register(Following)
admin.site.register(Users)
admin.site.register(Tweet)

# Register your models here.
