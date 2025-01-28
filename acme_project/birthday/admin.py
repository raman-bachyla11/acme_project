from django.contrib import admin
from .models import Birthday


admin.site.empty_value_display = 'Не задано'


@admin.register(Birthday) 
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday'
    )
    list_editable = (
        'first_name',
        'last_name'
    )
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name', 'birthday')
    list_display_links = ('birthday',)
