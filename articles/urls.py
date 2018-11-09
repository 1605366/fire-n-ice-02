from django.urls import path

from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name='index'),
    path('cart',views.CartPageView.as_view(),name='cart'),
    path('order',views.OrderPageView.as_view(),name='order'),
]
