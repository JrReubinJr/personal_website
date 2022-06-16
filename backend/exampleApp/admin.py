from django.contrib import admin
from .models import exampleApp

class ExampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(exampleApp, ExampleAdmin)


# Register your models here.
