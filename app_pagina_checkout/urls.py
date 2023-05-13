from django.urls import path
from app_pagina_checkout.views import checkout

urlpatterns = [
    path('', checkout, name='checkout'),
]
