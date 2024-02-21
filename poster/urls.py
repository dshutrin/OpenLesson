from django.urls import path
from .views import *


urlpatterns = [
    path('', welcome),
    path('login', login_view),
    path('register', register_view),
    path('logout', logout_view),
    path('home', home),
]
