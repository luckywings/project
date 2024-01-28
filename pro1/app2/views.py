from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import Cart, Product
from . models import Order, OrderItem
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def index(request):
    return render(request,"index.html")

def shop(request):
    return render(request,"shop.html")


def why(request):
    return render(request,"why.html")


def contact(request):
    return render(request,"contact.html")

def testimonial(request):
    return render(request,"testimonial.html")


def login(request):
    if 'signup' in request.POST:
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists!!!!")
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken!!!!")
            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save()
                return render(request,"login.html")
    if 'signin' in request.POST:
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                return render(request,"index.html")
            else:
                messages.info(request,"Invalid Username or Password!!!!")
    return render(request,"login.html")

def product(request):
    product=Product.objects.all()
    return render(request,"product.html",{"product":product})


def allproduct(request):
    
    return render(request,"allproduct.html")

def product_de(request):
    return render(request,"product_de.html")

def orders(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    if request.method=="POST":
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        address=request.POST['address']
        zipcode=request.POST['zipcode']
        place=request.POST['city']
        phone=request.POST['phone']
        paid_amount=request.POST['total']
        print(first_name)
        order=Order.objects.create(first_name=first_name,last_name=last_name,email=email,address=address,zipcode=zipcode,place=place,phone=phone,paid_amount=paid_amount)

    context = {
       "total_price":total_price 
    }
    return render(request, "orders.html",context)

   



def start_order(request):
    cart = Cart(request)

    if request.method == 'POST':
        username = request.POST.get('username')
       
        email = request.POST.get('email')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        place = request.POST.get('place')
        phone = request.POST.get('phone')

        order = Order.objects.create(user=request.user, username=username, email=email, phone=phone, address=address, zipcode=zipcode, place=place)

        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.total_price * quantity

            item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

        return redirect('product_list')
    return redirect('cart')



def cart(request):
    cart = Cart.objects.all()
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html',{"cart":cart,"total_price":total_price})
def remove_from_cart(request, item_id):
    cart_item = Cart.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cartpage')

def add_to_cart(request,id):
    product = Product.objects.get(id=id)
    cart_item, created = Cart.objects.get_or_create(product=product,user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cartpage')