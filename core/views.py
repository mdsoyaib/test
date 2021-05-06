from django.shortcuts import render

# Create your views here.
from django.views import View


# class Base(View):
#     def get(self, request):
#         return render(request, "core/base.html")


class Blog(View):
    def get(self, request):
        return render(request, "core/blog.html")


class BlogDetails(View):
    def get(self, request):
        return render(request, "core/blog_details.html")


class Checkout(View):
    def get(self, request):
        return render(request, "core/checkout.html")


class Contact(View):
    def get(self, request):
        return render(request, "core/contact.html")


class Index(View):
    def get(self, request):
        return render(request, "core/index.html")


class Shop(View):
    def get(self, request):
        return render(request, "core/shop.html")


class ShopDetails(View):
    def get(self, request):
        return render(request, "core/shop_details.html")


class ShopingCart(View):
    def get(self, request):
        return render(request, "core/shoping_cart.html")