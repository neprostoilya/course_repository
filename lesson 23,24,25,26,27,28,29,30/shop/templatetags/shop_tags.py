from django import template
from shop.models import Category, FavoriteProducts
from django.template.defaulttags import register as custom_range

register = template.Library() 

@register.simple_tag()
def get_subcategories(category):
    return Category.objects.filter(parent=category)

@register.simple_tag()
def get_sorted():
    """Сортировка по цене цвету размеру"""
    sorters = [
        {
            'title': 'По цене',
            'sorters': [
                ('price', 'По возрастанию'),
                ('-price', 'По убыванию')
            ]
        },
        {
            'title': 'По цвету',
            'sorters': [
                ('color', 'От А до Я'),
                ('-color', 'От Я до А')

            ]
        },
        {
            'title': 'Размер',
            'sorters': [
                ('size', 'От возростанию'),
                ('-size', 'От убыванию')
            ]
        }
    ]
    return sorters

@custom_range.filter
def get_range(value):
    return range(int(value))

@custom_range.filter
def get_remain(value):
    remain = 5 - int(value)
    return range(remain)

@register.simple_tag()
def get_favorite_products(user):
    """Вывод избранных товаров на страничку"""
    favorite = FavoriteProducts.objects.filter(user=user)
    products = [i.product for i in favorite]
    return products