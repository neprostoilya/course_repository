from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    """Перевод полей категории"""
    fields = ('title',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    """Перевод полей продукта"""
    fields = ('title', 'description', 'info')