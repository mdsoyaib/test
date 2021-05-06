"""clock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', views.Blog.as_view(), name="blog"),
    path('blog_details/', views.BlogDetails.as_view(), name="blog_details"),
    path('checkout/', views.Checkout.as_view(), name="checkout"),
    path('contact/', views.Contact.as_view(), name="contact"),
    path('', views.Index.as_view(), name="index"),
    path('shop/', views.Shop.as_view(), name="shop"),
    path('shop_details/', views.ShopDetails.as_view(), name="shop_details"),
    path('shoping_cart/', views.ShopingCart.as_view(), name="shoping_cart"),
]
