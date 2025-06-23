from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'email', 'full_name', 'role', 'department', 'year_of_study', 'gender', 'games', 'is_staff'
    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {
            'fields': (
                'full_name', 'role', 'department', 'year_of_study', 'gender', 'games'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2',
                'full_name', 'role', 'department', 'year_of_study', 'gender', 'games',
                'is_staff', 'is_active', 'is_superuser',
            ),
        }),
    )

    ordering = ('email',)
    search_fields = ('email', 'full_name', 'department')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')

admin.site.register(CustomUser, CustomUserAdmin)
