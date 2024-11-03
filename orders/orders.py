from abc import ABC, abstractmethod

from django.contrib import messages
from django.core.exceptions import ValidationError

from carts.models import Cart
from orders.models import OrderItem, Order


class OrderCreationTemplate(ABC):
    def create_order(self, request, form):
        order = self.create_order_instance(request.user, form)
        self.add_items_to_order(request.user, order)
        self.post_process_order(request, order)
        return order
    
    @abstractmethod
    def create_order_instance(self, user, form):
        pass

    @abstractmethod
    def add_items_to_order(self, user, order):
        pass

    @abstractmethod
    def post_process_order(self, user, order):
        pass



class DefaultOrderCreation(OrderCreationTemplate):
    def create_order_instance(self, user, form):
        return Order.objects.create(
            user=user,
            phone_number=form.cleaned_data["phone_number"],
            requires_delievery=form.cleaned_data["requires_delivery"],
            delievery_address=form.cleaned_data["delivery_address"],
            payment_on_get=form.cleaned_data["payment_on_get"]
        )

    def add_items_to_order(self, user, order):
        cart_items = Cart.objects.filter(user=user)
        for cart_item in cart_items:
            product = cart_item.product
            name = cart_item.product.name
            price = cart_item.product.sell_price()
            quantity = cart_item.quantity

            if product.quantity < quantity:
                raise ValidationError(f'Недостаточно количество товара {name} на складе. В наличии - {product.quantity}')

            OrderItem.objects.create(
                order=order,
                product=product,
                name=name,
                price=price,
                quantity=quantity,
            )
            product.quantity -= quantity
            product.save()

        cart_items.delete()

    def post_process_order(self, request, order):
        messages.success(request, "Заказ успешно создан")

