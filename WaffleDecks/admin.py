from django.contrib import admin
from .models import Deck, CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Deck)


class CustomUserAdmin(UserAdmin):
    pass


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'region',
        'comuna', 'direccion'
    )


admin.site.register(CustomUser, CustomUserAdmin)
