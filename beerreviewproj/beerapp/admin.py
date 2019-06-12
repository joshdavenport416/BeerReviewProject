from django.contrib import admin
from .models import BeerType, Beer, Review

# Register your models here.
admin.site.register(BeerType)
admin.site.register(Beer)
admin.site.register(Review)