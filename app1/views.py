from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Product,Cart,Glasses,WGlasses
from django.contrib.auth.models import User
from .forms import registerform
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import loginform
# Create your views here.
def regview(request):
    f1=registerform()
    if request.method=='POST':
        f1=registerform(request.POST)
        if f1.is_valid():
            print(f1)
            f1.save()
            return HttpResponse('form is submitted')
    return render(request,'reg.html',{'form':f1})

@login_required
def home(request):
    return render(request,'home.html')

def loginview(request):
    l1=loginform()
    if request.method=='POST':
        f1=loginform(request.POST)
        if f1.is_valid():
            username=f1.cleaned_data.get('username')
            password=f1.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,'home.html')
            else:
                return HttpResponse('invalid user')
    return render(request,'login.html',{'form':l1})


def home(request):
    sunglasses = Product.objects.filter(category='Sunglasses')  # Fetch Sunglasses
    eyeglasses = Product.objects.filter(category='Eyeglasses')  # Fetch Eyeglasses
    return render(request, 'home.html', {'sunglasses': sunglasses, 'eyeglasses': eyeglasses})

def sunglass(request):
    products = Product.objects.filter(category='Sunglasses')
    return render(request,'sunglass.html',{'products': products})

def eyeglassess(request):
    products =  Product.objects.filter(category='Eyeglasses')
    return render(request,'eyeglassess.html', {'products': products})

def termsandconditions(request):
    return render(request,'termsandconditions.html')

def contact(request):
    return render(request,'contact.html')

def product_detail(request, id):
    # Try to get the product from both tables
    product = None
    product_type = None

    try:
        product = Product.objects.get(id=id)
        product_type = 'product'
    except Product.DoesNotExist:
        try:
            product = Glasses.objects.get(id=id)
            product_type = 'glasses'
        except Glasses.DoesNotExist:
            # Return a 404 page if not found in either table
            return render(request, '404.html')

    return render(request, 'product_detail.html', {'product': product, 'product_type': product_type})

def view(request,id):
    products = Product.objects.get(id=id) 
    return render(request,'view_card.html',{'products': products})

def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('app1:login')

    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

def delete(request, id):
    cart_item = get_object_or_404(Cart, id=id)
    cart_item.delete()
    return redirect('app1:view_cart') 

def womenglasses(request):
    glasses = WGlasses.objects.all()
    return render(request,'womenglasses.html',{'glasses': glasses})

def menglasses_list(request):
    glasses = Glasses.objects.all()
    return render(request,'menglasses.html',{'glasses': glasses})

def add_to_cart(request, id):
    if not request.user.is_authenticated:
        return redirect('app1:login')  # Redirect to login if not authenticated

    user = request.user
    product = None
    glasses = None
    wglasses = None

    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        try:
            glasses = Glasses.objects.get(id=id)
        except Glasses.DoesNotExist:
            try:
                wglasses = WGlasses.objects.get(id=id)
            except WGlasses.DoesNotExist:
                return redirect('app1:home')

    cart_item, created = Cart.objects.get_or_create(
        user=user,
        product=product if product else None,
        glasses=glasses if glasses else None,
        wglasses=wglasses if wglasses else None,
        defaults={'quantity': 1}  # Default quantity when first added
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('app1:view_cart')  # Redirect to view cart


def update_quantity(request, id):
    # Get the cart item
    cart_item = get_object_or_404(Cart, id=id)
    
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity'))
        
        if new_quantity > 0:
            cart_item.quantity = new_quantity
            cart_item.save()
        else:
            return HttpResponse("Invalid quantity.", status=400)
    
    return redirect('app1:view_cart')  # Redirect to the cart view page
