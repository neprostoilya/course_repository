from random import randint

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib import messages
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect
import stripe

from .forms import LoginForm, RegistrationForm, ReviewForm, CustomerForm, ShippingForm
from .models import Category, Product, Review, FavoriteProducts, Mail, Customer
from .utils import CartForAuthenticated, get_cart_data, get_fav_and_cart
from .tasks import send_message, send_spam_text
from conf import settings


class Page(ListView):
    """Главная страница"""

    model = Product
    context_object_name = 'categories'
    extra_context = {
        'title': 'Главная страница',
    }
    template_name = 'shop/index.html'


    def get_queryset(self):
        """Вывод родительских категорий"""
        categories = Category.objects.filter(
            parent=None
        )
        return categories
    
    def get_context_data(self, **kwargs):
        """Вывод дополнительных элементов на главную страничку"""
        context = super().get_context_data()
        context['top_products'] = Product.objects.order_by('-watched')[:8]
        context['cart_and_fav'] = get_fav_and_cart(self.request)
        return context

class SubCategoryPage(ListView):
    """Вывод подкатегорий на отдельной странице"""
    model = Product
    paginate_by = 2
    context_object_name = 'products'
    template_name = 'shop/category_page.html'

    def get_queryset(self):
        """Получение всех товаров по категории"""
        type_field = self.request.GET.get('type')
        if type_field:
            products = Product.objects.filter(category__slug=type_field)
            return products
        parent_category = Category.objects.get(
            slug=self.kwargs['slug']
        )   
        subcategories = parent_category.subcategories.all()
        products = Product.objects.filter(
            category__in=subcategories).order_by('?')
        
        sort_field = self.request.GET.get('sort')
        if sort_field:
            products = products.order_by(sort_field)
        return products
    
    def get_context_data(self, **kwargs):
        """Вывод дополнительных элементов на страничку"""
        context = super().get_context_data()
        parent_category = Category.objects.get(
            slug=self.kwargs['slug']
        )
        context['category'] = parent_category
        context['title'] = parent_category.title
        context['cart_and_fav'] = get_fav_and_cart(self.request)
        return context
    

class ProductPage(DetailView):
    """Вывод товара на отдельной странице"""
    model = Product
    context_object_name = 'product'
    template_name = 'shop/product_page.html'

    def get_context_data(self, **kwargs):
        """Вывод дополнительных элементов на страничку"""
        context = super().get_context_data()
        product = Product.objects.get(
            slug=self.kwargs['slug']
        )
        context['title'] = product.title    
        products = Product.objects.filter(category=product.category)
        data = []
        for count in range(5):
            random_index = randint(0, len(products)-1)
            random_product = products[random_index]
            if random_product not in data and str(random_product) != product.title:
                data.append(random_product)
        context['products'] = data
        context['reviews'] = Review.objects.filter(product=product).order_by('-pk')
        context['cart_and_fav'] = get_fav_and_cart(self.request)
        return context
    
def login_registration(request):
    """Регистрация пользователя"""
    context = {
        'title': 'Зарегистрироваться',
        'registration_form': RegistrationForm()
    }

    return render(request, 'shop/login_registration.html', context)

def login_authentication(request):
    """Аутендификации пользователя"""
    context = {
        'title': 'Войти',
        'login_form': LoginForm()
    }

    return render(request, 'shop/login_authentication.html', context)


def user_login(request):
    """Вход в аккаунт"""
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('index')
    else:
        messages.error(request, 'Не верное имя пользователя или пароль')
        return redirect('login_authentication')

def user_logout(request):
    """Выход из аккаунта"""
    logout(request)
    return redirect('index')

def register(request):
    """Регистрация аккаунта"""
    form = RegistrationForm(data=request.POST)
    if form.is_valid():
        print(form)
        form.save()
        messages.success(request, 'Аккаунт успешно создан. Войдите в аккаунт')
    else:
        for error in form.errors:
            print(form.errors[error].as_text())
            messages.error(request, form.errors[error].as_text())

    return redirect('login_registration')

def save_review(request, product_id):
    """Cохранения отзыва"""
    form = ReviewForm(data=request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user
        product = Product.objects.get(pk=product_id)
        review.product = product
        review.save()
        return redirect('product_page', product.slug)

def save_favorite_product(request, product_slug):
    """Удаление или добавление избранных товаров"""
    user = request.user if request.user.is_authenticated else None
    product = Product.objects.get(slug=product_slug)
    favorite_products = FavoriteProducts.objects.filter(user=user)
    if user:
        if product in [i.product for i in favorite_products]:
            fav_product = FavoriteProducts.objects.get(user=user, product=product)
            fav_product.delete()
        else:
            FavoriteProducts.objects.create(user=user, product=product)
    next_page = request.META.get('HTTP_REFERER', 'products_list')
    return redirect(next_page)

class FavoriteProductsView(LoginRequiredMixin, ListView):
    """Вывод избранных товаров на страничку"""
    model = FavoriteProducts
    context_object_name = 'products'
    template_name = 'shop/favorite_products.html'
    login_url = 'login_registration'

    def get_queryset(self):
        """Получаем товары конкретного пользователя"""
        user = self.request.user
        favorite_products = FavoriteProducts.objects.filter(
            user=user
        )
        products = [_.product for _ in favorite_products]
        return products
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['cart_and_fav'] = get_fav_and_cart(self.request)
        return context

def save_mail(request):
    """Собиратель почтовых адресов"""
    email = request.POST.get('email')
    user = request.user if request.user.is_authenticated else None
    if email:
        try:
            Mail.objects.create(mail=email, user=user)
            send_message.delay(email)
        except:
            pass
    return redirect('index')

def send_mail_to_customers(request):
    """Рассылка писем"""
    if request.method == 'POST':
        text = request.POST.get('text')
        send_spam_text.delay(text)
    context = {'title': 'Спаммер'}
    return render(request, 'shop/send_mail.html', context)

def cart(request):
    """Страница корзины"""
    if request.user.is_authenticated:
        cart_info = get_cart_data(request)
        context = {
            'title': 'Корзина', 
            'order': cart_info['order'],
            'order_products': cart_info['order_products'],
            'cart_total_quantity': cart_info['cart_total_quantity'], 
            'cart_total_price': cart_info['cart_total_price'],
            'cart_and_fav': get_fav_and_cart(request)
        }
        return render(request, 'shop/cart.html', context)

    
def to_cart(request, product_id, action):
    """Добавление товара в корзинку"""
    if request.user.is_authenticated:
        CartForAuthenticated(
            request,
            product_id,
            action,
        )
        return redirect('cart')
    else:
        messages.error(request, 'Авторизуйтесь или зарегистрируйтесь, чтобы совершать покупки')
        return redirect('login_registration')
    
def checkout(request):
    """Страница офорления заказа"""
    cart_info = get_cart_data(request)

    context = {
        'title': 'Оформление заказа',
        'order': cart_info['order'],
        'order_products': cart_info['order_products'],
        'cart_total_quantity': cart_info['cart_total_quantity'],
        'customer_form': CustomerForm(),
        'shipping_form': ShippingForm(),
        'cart_and_fav': get_fav_and_cart(request)
    }
    return render(request, 'shop/checkout.html', context)

def create_checkout_session(request):
    """Оплата через VISA"""
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        user_cart = CartForAuthenticated(request)
        cart_info = user_cart.get_cart_info()

        customer_form = CustomerForm(data=request.POST)
        if customer_form.is_valid():
            customer = Customer.objects.get(user=request.user)
            customer.first_name = customer_form.cleaned_data['first_name']
            customer.last_name = customer_form.cleaned_data['last_name']
            customer.email = customer_form.cleaned_data['email']
            customer.phone = customer_form.cleaned_data['phone']
            customer.save()

        shipping_form = ShippingForm(data=request.POST)
        if shipping_form.is_valid():
            address = shipping_form.save(commit=False)
            address.customer = Customer.objects.get(user=request.user)
            address.order = user_cart.get_cart_info()['order']
            address.save()

        total_price = cart_info['cart_total_price']
        total_quantity = cart_info['cart_total_quantity']

        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': 'Shop'},
                    'unit_amount': int(total_price * 100)
                },
                'quantity': total_quantity
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')),
            cancel_url=request.build_absolute_uri(reverse('success'))
        )
        return redirect(session.url, 303)

    
def successPayment(request):
    """Оплата прошла успешно"""
    user_cart = CartForAuthenticated(request)
    user_cart.clear()
    context = {
        'title': 'Оплата',
    }
    messages.success(request, 'Оплата прошла успешно')
    return render(request, 'shop/success.html', context)

