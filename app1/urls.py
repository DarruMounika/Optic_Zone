from django.urls import path
from .views import *
from . import views

app_name = 'app1'
urlpatterns = [
    path('',home,name='home'),
    path('reg/',regview,name='reg'),
    path('login/',loginview,name='login'),
    path('home/',home,name='home'),
    path('sunglass/',sunglass,name='sunglass'),
    path('eyeglassess/',eyeglassess,name='eyeglassess'),
    path('termsandconditions/',termsandconditions,name='termsandconditions'),
    path('contact/', contact, name='contact'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('cart/', views.view_cart, name='view_cart'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update-quantity/<int:id>/', views.update_quantity, name='update_quantity'),
    path('view',view,name='view'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('womenglasses/',womenglasses,name='womenglasses'),
    path('glasses/', menglasses_list, name='menglasses_list')   
    ]

