from django.contrib import admin

from .models import Place
admin.site.register(Place)

from .models import Port
admin.site.register(Port)
