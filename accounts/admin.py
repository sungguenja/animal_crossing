from django.contrib import admin
from .models import Villagers, Fish, Bug, User
# Register your models here.
admin.site.register(Villagers)
admin.site.register(Fish)
admin.site.register(Bug)
admin.site.register(User)