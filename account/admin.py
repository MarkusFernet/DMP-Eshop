from django.contrib import admin
from .models import Customer

# admin.site.register(Customer)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'id',]
    # list_filter = ['in_stock', 'is_active']
    # list_editable = ['price', 'in_stock']
    # prepopulated_fields = {'slug': ('title',)}
