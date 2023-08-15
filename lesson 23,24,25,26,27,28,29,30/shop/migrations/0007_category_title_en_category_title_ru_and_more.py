# Generated by Django 4.2.3 on 2023-08-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_customer_order_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Название категории'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Название категории'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(default='Здесь скоро будет описание', null=True, verbose_name='Описание товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(default='Здесь скоро будет описание', null=True, verbose_name='Описание товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='info_en',
            field=models.TextField(default='Дополнительная информация о продукте', null=True, verbose_name='Информация о товаре'),
        ),
        migrations.AddField(
            model_name='product',
            name='info_ru',
            field=models.TextField(default='Дополнительная информация о продукте', null=True, verbose_name='Информация о товаре'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название товара'),
        ),
    ]