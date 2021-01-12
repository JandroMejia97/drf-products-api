from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'main',)
    list_display_links = ('name',)
    list_select_related = ('main',)
    search_fields = ('name',)
    list_filter = [('main', admin.RelatedOnlyFieldListFilter)]
    fieldsets = (
        (_('Category'), {
            'fields': (
                'main',
                'name',
            ),
        }),
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    fieldsets = (
        (_('Brand'), {
            'fields': (
                'name',
            ),
        }),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category',)
    list_display_links = ('name',)
    search_fields = ('name', 'category__name', 'brand__name',)
    list_select_related = ('brand', 'category',)
    list_filter = [
        'is_new',
        ('category', admin.RelatedOnlyFieldListFilter),
        ('brand', admin.RelatedOnlyFieldListFilter),
    ]
    fieldsets = (
        (_('Info'), {
            'fields': (
                'name',
                'brand',
                'category',
                'is_new',
                'model',
                'url',
                'image_url',
            )
        }),
        (_('Price'), {
            'fields': (
                'current_price',
                'raw_price',
                'discount',
            )
        }),
    )


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'color',)
    list_display_links = ('product',)
    search_fields = ('product__name',)
    fieldsets = (
        (_('Variation'), {
            'fields': (
                'product',
                'color',
                'thumbnail_url',
                'image_url',
            ),
        }),
    )
