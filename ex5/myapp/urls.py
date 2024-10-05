# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_session_view, name='user_session_view'),  # URL to access the view
]
