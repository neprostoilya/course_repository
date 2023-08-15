from django.contrib import messages
from django.shortcuts import redirect

from .models import Order, OrderProduct, Customer, Product, FavoriteProducts

class CartForAuthenticated:
    """Логика корзины"""

    def __init__(self, request, product_id=None, action=None) -> None:
        self.user = request.user
        if action and product_id:
            self.add_or_delete_product(product_id, action)

    def get_cart_info(self):
        """Получение информациии с корзины (колл-во и сумма товаров) и заказчике"""
        custumer, _ = Customer.objects.get_or_create(
            user=self.user
        )
        order, _ = Order.objects.get_or_create(
            custumer=custumer
        )
        order_products = order.ordered.all()
        cart_total_quantity = order.get_cart_total_quantity
        cart_total_price = order.get_cart_total_price
        return {
            'order': order,
            'order_products': order_products,
            'cart_total_quantity': cart_total_quantity, 
            'cart_total_price': cart_total_price
        }

    def add_or_delete_product(self, product_id, action):
        """Добавление и удаление товаров с корзинки по нажатию на кнопки + и -"""
        order = self.get_cart_info()['order'] 
        product = Product.objects.get(
            pk=product_id
        )
        order_product, _ = OrderProduct.objects.get_or_create(
            order=order,
            product=product
        )
        if action == 'add' and product.quantity > 0:
            order_product.quantity += 1 # -1 в корзинке
            product.quantity -= 1 # -1 на складе
        elif action == 'delete':
            order_product.quantity -= 1 # -1 в корзинке
            product.quantity += 1 # -1 на складе
        elif action == 'remove':
            product.quantity += order_product.quantity
            order_product.quantity -= order_product.quantity

        order_product.save()
        product.save()
        if order_product.quantity < 1:
            order_product.delete()

    def clear(self):
        """Удаление всех товаров после оплаты"""
        order = self.get_cart_info()['order']
        order_products = order.ordered.all()
        for product in order_products:
            product.delete()
        order.save()

            
def get_cart_data(request):
    """Вывод товара с корзинки на страничку"""
    cart = CartForAuthenticated(request)
    cart_info = cart.get_cart_info()
    return {
        'order': cart_info['order'],
        'order_products': cart_info['order_products'],
        'cart_total_quantity': cart_info['cart_total_quantity'], 
        'cart_total_price': cart_info['cart_total_price']
    }

def get_fav_and_cart(request):
    if request.user.is_authenticated:
        cnt_fav = len(FavoriteProducts.objects.filter(
            user=request.user
        ))
        cart_info = get_cart_data(request)
        cnt_cart = cart_info['cart_total_quantity']
        return {
            'cnt_fav': cnt_fav,
            'cnt_cart': cnt_cart
        }
    else:
        messages.error(request, 'Авторизуйтесь или Зарегистрируйтесь чтобы совершать покупки!')
        return redirect('login_registration')
    