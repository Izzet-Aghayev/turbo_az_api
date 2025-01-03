from django.contrib import admin

from accounts.models import User



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name')
    search_fields = ('email',)
    list_per_page = 15
