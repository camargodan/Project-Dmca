from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username', ]
    prepopulated_fields = {'slug': ('username',)}
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'imag_clie')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'is_client', 'is_worker', 'assign')}),
        ('Login info', {'fields': ('date_joined', 'last_login', 'slug',)}),
    )
    prepopulated_fields = {'slug': ('username',)}


admin.site.register(User, CustomUserAdmin)
