from django.shortcuts import render, HttpResponse
from .models import contact
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .models import Product, CartItem, Cart
import stripe
from django.conf import settings


def index(request):
    return render(request, 'myapp/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dec = request.POST.get('dec')
        con = contact(name=name, email=email, phone=phone, dec=dec)
        con.save()
        messages.success(request, 'Your message has been sent')

    return render(request, 'myapp/contacts.html')


def about(request):
    return render(request, 'myapp/about.html')


def services(request):
    return render(request, 'myapp/services.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'myapp/register.html', {'form': form})


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрированы!')
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#
#     return render(request, 'myapp/register.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Регистрация прошла успешно. Добро пожаловать, {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})


def basket(request):
    cart = Cart.objects.first()

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity = quantity
        cart_item.price = product.price
        cart_item.save()

        cart.total_price = sum(item.quantity * item.price for item in cart.items.all())
        cart.save()

    context = {'cart': cart}
    return render(request, 'cart.html', context)


stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_secret = settings.STRIPE_PUBLISHABLE_KEY



def checkout(request):
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        amount = 1000

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='uzs',
                source=token,
            )



            return render(request, 'checkout_success.html')
        except stripe.error.CardError as e:
            error_message = e.error.message
            return render(request, 'checkout.html', {'error_message': error_message})

    return render(request, 'myapp/checkout.html')
