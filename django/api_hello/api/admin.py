from django.contrib import admin

from .models import Filme


# Register your models here.
class FilmeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Filme, FilmeAdmin)
