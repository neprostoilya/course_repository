from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from .models import Product, Category, Gallery, Review, FavoriteProducts, Mail, \
    Customer, Order, OrderProduct, ShippingAddress

class GalleryInline(admin.TabularInline):
    """Галерея товаров"""
    fk_name = 'product'
    model = Gallery
    extra = 1


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    """Категории"""
    list_display = ('pk', 'title', 'parent', 'get_products_count')
    prepopulated_fields = {'slug': ('title',)}

    def get_products_count(self, obj):
        if obj.products:
            return str(len(obj.products.all()))
        else:
            return 0

    get_products_count.short_description = 'Количество товаров'


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    """Товары"""
    list_display = ('pk', 'title', 'category', 'quantity', 'price', 'created_at', 'size', 'color', 'get_photo')
    list_editable = ('price', 'quantity', 'size', 'color')
    readonly_fields = ('watched',)
    list_display_links = ('title', 'pk')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'price')
    inlines = (GalleryInline,)

    def get_photo(self, obj):
        """Отображение миниатюры"""
        if obj.images.all():
            return mark_safe(f'<img src="{obj.images.all()[0].image.url}" width="75">')

        else:
            return '-'

    get_photo.short_description = 'Миниатюра'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ('pk', 'author', 'created_at')
    readonly_fields = ('author', 'text', 'created_at')
    
@admin.register(Mail)
class ReviewEmail(admin.ModelAdmin):
    """Почтовые адреса"""
    list_display = ('pk', 'mail', 'user')
    readonly_fields = ('mail', 'user')
    list_filter = ('user',)

@admin.register(FavoriteProducts)
class ReviewFavorite(admin.ModelAdmin):
    """Избранные товары"""
    list_display = ('user', 'product')
    readonly_fields = ('user', 'product')
    list_filter = ('product',)

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(ShippingAddress)
admin.site.register(Gallery)
