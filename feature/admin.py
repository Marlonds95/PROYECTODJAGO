from django.contrib import admin
from .models import Feature
# Register your models here.
class FeatureAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Feature, FeatureAdmin)
