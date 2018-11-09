from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

class CartPageView(TemplateView):
    template_name = 'cart.html'

class OrderPageView(TemplateView):
    template_name = 'order.html'
