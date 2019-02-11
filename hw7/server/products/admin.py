from datetime import datetime
from django.contrib import admin
from django.template.loader import render_to_string
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'is_new', 'name', 'category',
        'image', 'cost', 'modified', 'created'
    ]

    list_filter = [
        'category', 'image',
        'modified', 'created'
    ]

    search_fields = [
        'name', 'description'
    ]

    fieldsets = (
        (
            'Default', {
                'fields': ('name', 'category',)
            }
        ),
        (
            'Content', {
                'fields': ('image', 'description', 'cost')
            }
        ),
    )

    def picture(self, obj):
        return render_to_string(
            'products/components/picture.html',
            {'url': obj.image.url}
        )

    def is_new(self, obj):
        return datetime.now().date() == obj.created.date()

# Register your models here.
# admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
