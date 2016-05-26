from django.contrib import admin

# Register your models here.
from store.models import OnlineStore, Products

'''Register models for admin'''


admin.site.register(OnlineStore)
admin.site.register(Products)