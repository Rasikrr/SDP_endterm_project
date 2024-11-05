from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect, render
from django.urls import reverse, reverse_lazy
from main.decorators import log_request
from orders.models import Order, OrderItem
from users.forms import CreateUserForm, FormFactory, LoginForm, ProfileForm
from users.models import CustomUser
from users.services import (
    add_anonymous_user_cart,
    generate_context,
    profile_edit_service,
    signin_service,
    signup_service,
)


def signin(request):
    if request.method == "POST":
        form = FormFactory.create_form("login", request.POST)
        user = signin_service(form=form)
        if user:
            auth.login(request, user)

            add_anonymous_user_cart(request=request, user=user)

            messages.success(request, "Вы успешно вошли в аккаунт")
            redirect_page = request.POST.get("next", None)
            if redirect_page and redirect_page != reverse("user:logout"):
                return redirect(redirect_page)
            return redirect("main:index")
        else:
            messages.warning(request, "Неверная почта или пароль")
            return redirect("user:signin")
    else:
        form = FormFactory.create_form("login")
    context = generate_context(form=form)
    return render(request, "signin.html", context=context)


def registration(request):
    if request.method == "POST":
        form = FormFactory.create_form("signup", request.POST)
        user = signup_service(form)
        if user:

            add_anonymous_user_cart(request=request, user=user)

            auth.login(request, user, backend="users.backends.EmailBackEnd")
            messages.success(request, "Вы успешно зарегестрированы и вошли в аккаунт")
            return redirect("main:index")
    else:
        form = FormFactory.create_form("signup")
    context = generate_context(form=form)
    return render(request, "registration.html", context=context)


@login_required
def profile(request):
    if request.method == "POST":
        form = FormFactory.create_form(
            "profile", request.POST, instance=request.user, files=request.FILES
        )
        response = profile_edit_service(form)
        if response:
            messages.success(request, "Данные успешно обновлены")
            return redirect("user:profile")
    else:
        form = FormFactory.create_form("profile", instance=request.user)
    user_orders = Order.objects.filter(user=request.user)
    orders_items = OrderItem.objects.filter(order__in=user_orders)
    order_with_items = {}
    for order in user_orders:
        order_with_items[order] = []

    overall = 0.0
    for item in orders_items:
        overall += float(item.quantity) * float(item.price)
        order_with_items[item.order].append(item)
    orders = []
    for order in order_with_items:
        orders.append([order, order_with_items[order]])
    context = generate_context(form=form)
    context["orders"] = orders
    context["overall"] = round(overall, 2)
    return render(request, "profile.html", context=context)


def users_cart(request):
    return render(request, "users/users_cart.html")


def logout(request):
    auth.logout(request)
    messages.success(request, "Вы успешно вышли из аккаунты")
    return redirect("main:index")
