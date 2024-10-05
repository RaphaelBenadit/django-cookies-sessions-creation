# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('set_cookie/', views.set_cookie_view, name='set_cookie_view'),
    path('get_cookie/', views.get_cookie_view, name='get_cookie_view'),
]
