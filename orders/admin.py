from django.contrib import admin

from .models import BurritoBowl, BurritoWrap, Toppings, Subs

# Register your models here.
admin.site.register(BurritoBowl)
admin.site.register(BurritoWrap)
admin.site.register(Toppings)
admin.site.register(Subs)
