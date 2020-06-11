from django.contrib import admin
from .models import design, artwork, song, fossil_category, fossil
# Register your models here.
admin.site.register(design)
admin.site.register(artwork)
admin.site.register(song)
admin.site.register(fossil_category)
admin.site.register(fossil)