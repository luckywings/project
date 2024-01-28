"""
URL configuration for pro1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app2  import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="indexpage"),
    path('shop/',views.shop,name="shoppage"),
    path('contact/',views.contact,name="contactpage"),
    path('why/',views.why,name="whypage"),
    path('testimonial/',views.testimonial,name="testimonialpage"),
    path('login/',views.login,name="loginpage"),
    path('product/',views.product,name="productpage"),
    path('allproduct/',views.allproduct,name="allproductpage"),
    path('product_de/',views.product_de,name="product_depage"),
    path('add_to_cart/<int:id>/', views.add_to_cart, name="add_to_cart"),
    path('start_order/', views.start_order, name='start_order'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
   
    path('cart/',views.cart,name="cartpage"),
    path('orders/',views.orders,name="orders"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


