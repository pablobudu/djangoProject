from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Deck

# Esta clase nos permite mostrar los detalles del usuario en el /admin


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('region', 'comuna', 'direccion')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ()
        })
    )


admin.site.register(Deck)
admin.site.register(CustomUser, CustomUserAdmin)
