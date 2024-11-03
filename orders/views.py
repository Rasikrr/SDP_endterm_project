from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import redirect, render

from orders.forms import CreateOrderForm
from orders.orders import DefaultOrderCreation
from users.services import generate_context


@login_required
def create_order(request):
    if request.method == "POST":
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    order_creator = DefaultOrderCreation()
                    order_creator.create_order(request, form)
                    return redirect("main:index")
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect("cart:order")
    else:
        initial = generate_context(first_name=request.user.first_name, last_name=request.user.last_name)
        form = CreateOrderForm(initial=initial)

    context = generate_context(title="Home: Оформление заказа", form=form, order=True)
    return render(request, "orders/create_order.html", context=context)