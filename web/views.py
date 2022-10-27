from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from web.forms import RegistrationForm

from web.models import User, Products


# Create your views here.
def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User(
                email=email
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
            login(request, user)
    return render(request, "web/registration1.html", {
        "form": form,
        'is_success': is_success
    })


def product_add(request):
    error = None
    name, price, description, picture = '', '', '', ''
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        if not name:
            error = 'Поле название не заполнено '
        elif not price:
            error = 'Поле цена не заполнено '
        elif not description:
            error = 'Поле описание не заполнено '
        else:
            product = Products.objects.create(name=name,
                                              description=description,
                                              price=price)
            return redirect('product', product.id)

    return render(request, "web/product_add.html", {'error': error,
                                                    'name': name,
                                                    'description': description,
                                                    'price': price})


def products(request, id):
    get_object_or_404(Products, id=id)
    products = Products.objects.get(id=id)
    return render(request, 'web/products.html', {"products": products})


def menu(request):
    products = Products.objects.all()
    return render(request, 'web/1.html', {"products": products})


def toys(request):
    return render(request, 'web/2.html')


def sets(request):
    return render(request, 'web/3.html')


def stocks(request):
    return render(request, 'web/4.html')


def process(request):
    return render(request, 'web/5.html')


def login_view(request):
    form = RegistrationForm()
    message = None
    if request.method == 'GET':
        form = RegistrationForm(request.GET)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is None:
                message = "Электронная почта или пароль неправильные"
            else:
                login(request, user)
                next_url = 'menu'
                if 'next' in request.GET:
                    next_url = request.GET.get("next")
                return redirect(next_url)
    return render(request, "web/login.html", {
        "form": form,
        'message': message
    })


def logout_view(request):
    logout(request)
    return redirect('menu')