from django.urls import path


from web.views import menu, toys, sets, stocks, process, login_view, logout_view, registration_view, products, \
    product_add


urlpatterns = [
    path('', menu, name='menu'),
    path('menu/', menu, name='menus'),
    path('menu/<int:id>/', products, name='product'),
    path('menu/add', product_add, name="product_add"),
    path('menu/toys/', toys),
    path('menu/sets/', sets),
    path('menu/stocks/', stocks),
    path('menu/process/', process),
    path("registration/", registration_view, name='registration'),
    path("login/", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
]