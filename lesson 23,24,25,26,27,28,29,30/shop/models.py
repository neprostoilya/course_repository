from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    """Категории товаров"""
    title = models.CharField(
        max_length=150, 
        verbose_name='Название категории'
    )
    image = models.ImageField(
        upload_to='categories/', 
        null=True, blank=True, 
        verbose_name='Изображение'
    )
    slug = models.SlugField(
        unique=True, 
        null=True
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Категория',
        related_name='subcategories'
    )
    def get_absolute_url(self):
        """Ссылка на страницу категорий"""
        return reverse('category_detail', kwargs={'slug': self.slug })

    def get_parent_category_photo(self):
        """Для получения картинки родительских категорий"""
        if self.image:
            return self.image.url
        else:
            return 'https://itaros.ru/upload/iblock/81b/lyrg5fswe4xqjb5i4pjmy2ojl0vjnv1o/a80973cf_2379_11eb_8dca_005056000e85_f2197ea0_3318_11ec_9700_20106a300d87.jpg'

    def __str__(self):
        """Строковое представление"""
        return self.title

    def __repr__(self):
        """Подобие строкового представления"""
        return f'Категория: pk={self.pk}, title={self.title}'

    class Meta:
        """Характер Класса"""
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    """Товары"""
    title = models.CharField(
        max_length=255, 
        verbose_name='Название товара'
    )
    price = models.FloatField(
        verbose_name='Цена'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания'
    )
    watched = models.IntegerField(
        default=0, 
        verbose_name='Просмотры'
    )
    quantity = models.IntegerField(
        default=0, 
        verbose_name='Количество на складе'
    )
    description = models.TextField(
        default='Здесь скоро будет описание', 
        verbose_name='Описание товара'
    )
    info = models.TextField(
        default='Дополнительная информация о продукте', 
        verbose_name='Информация о товаре'
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        verbose_name='Категория', 
        related_name='products'
    )
    slug = models.SlugField(
        unique=True, 
        null=True
    )
    size = models.IntegerField(
        default=30, 
        verbose_name='Размер в мм'
    )
    color = models.CharField(
        max_length=30, 
        default='Серебро', 
        verbose_name='Цвет/Материал'
    )

    def get_absolute_url(self):
        """Ссылка на страницу категорий"""
        return reverse('product_page', kwargs={'slug': self.slug })

    def get_first_photo(self):
        if self.images.first():
            return self.images.first().image.url
        else:
            return 'https://itaros.ru/upload/iblock/81b/lyrg5fswe4xqjb5i4pjmy2ojl0vjnv1o/a80973cf_2379_11eb_8dca_005056000e85_f2197ea0_3318_11ec_9700_20106a300d87.jpg'

    def __str__(self):
        """Строковое представление"""
        return self.title

    def __repr__(self):
        """Подобие строкового представления"""
        return f'Товар: pk={self.pk}, title={self.title} price={self.price}'

    class Meta:
        """Характер Класса"""
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Gallery(models.Model):
    """Картинки товаров"""
    image = models.ImageField(
        upload_to='products/', 
        verbose_name='Изображение'
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='images'
    )

    class Meta:
        """Характер Класса"""
        verbose_name = 'Изображение'
        verbose_name_plural = 'Галерея товаров'


DEFAULT_CHOICES = (
    ('5', 'Отлично'),
    ('4', 'Хорошо'),
    ('3', 'Нормально'),
    ('2', 'Плохо'),
    ('1', 'Ужасно'),
)

class Review(models.Model):
    """Отзывы товаров"""
    grade = models.CharField(
        max_length=20, 
        choices=DEFAULT_CHOICES, 
        blank=True, 
        null=True, 
        verbose_name='Оценка'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        verbose_name='Автор'
    )
    text = models.TextField(
        verbose_name='Текст отзыва'
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        verbose_name='Товар'
    )
    created_at = models.DateField(
        auto_now=True, 
        verbose_name='Дата'
    )

    def __str__(self) -> str:
        """Строковое представление"""
        return self.author.username
    
    class Meta:
        """Характер Класса"""
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class FavoriteProducts(models.Model):
    """Избранные товары"""
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Пользователь'
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        verbose_name="Избранные товары"
    )

    def __str__(self) -> str:
        """Строковое представление"""
        return self.product.title
    
    class Meta:
        """Характер Класса"""
        verbose_name = 'Избранные товар'
        verbose_name_plural = 'Избранные товары'

class Mail(models.Model):
    """Почтовые адреса"""
    mail = models.EmailField(
        unique=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        """Строковое представление"""
        return self.mail
    
    class Meta:
        """Характер Класса"""
        verbose_name = 'Почту'
        verbose_name_plural = 'Почтовые адреса'

class Customer(models.Model):
    """Контактная информация заказчика"""
    user = models.OneToOneField(
        User, 
        models.SET_NULL, 
        null=True,
        blank=True,
        verbose_name='Пользователь'
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name='Фамилия'
    )
    email = models.EmailField(
        verbose_name='Почтовый адрес'
    )
    phone = models.CharField(
        max_length=30,
        verbose_name='Телефоный Номер'
    )

    def __str__(self) -> str:
        """Строковое представление"""
        return self.first_name
    
    class Meta:
        """Характер Класса"""
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

class Order(models.Model):
    """Корзинка"""
    custumer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Покупатель'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата'
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name='Статус'
    )
    shiping = models.BooleanField(
        default=False,
        verbose_name='Доставка'
    )

    def __str__(self) -> str:
        """Строковое представление"""
        return str(self.pk)
    
    class Meta:
        """Характер Класса"""
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    @property # используется для создания <<специальной>> функциональности определеным методам
    def get_cart_total_price(self):
        """Для получения суммы товаров с корзины"""
        order_products = self.ordered.all()
        total_price = sum(
            [product.get_total_price for product in order_products]
        )
        return total_price
    
    @property # используется для создания <<специальной>> функциональности определеным методам
    def get_cart_total_quantity(self):
        """Для получения колличевства товаров с корзины"""
        order_products = self.ordered.all()
        total_quantity = sum(
            [product.quantity for product in order_products]
        )
        return total_quantity
        
class OrderProduct(models.Model):
    """Привязка продукта к козрине (много ко многим)"""
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True,
        related_name='ordered'
    )
    quantity = models.IntegerField(
        default=0,
        null=True,
        blank=True
    )
    added_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        """Характер Класса"""
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказах'

    @property # используется для создания <<специальной>> функциональности определеным методам
    def get_total_price(self):
        """Подсчитывает свою общую цену всех товаров"""
        total_price = self.product.price * self.quantity
        return total_price
    

class ShippingAddress(models.Model):
    """Адреса доставки"""
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.SET_NULL, 
        null=True
    )
    order = models.ForeignKey(
        Order, 
        on_delete=models.SET_NULL,
        null=True
    )
    city = models.CharField(
        max_length=255
    )   
    state = models.CharField(
        max_length=255
    )   
    street = models.CharField(
        max_length=255
    )  
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """Строковое представление"""
        return self.street

    class Meta:
        """Характер Класса"""
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса доставки'