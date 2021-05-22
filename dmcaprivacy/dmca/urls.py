from django.urls import path
from .views import Loginview, Administrator, Worker, User


urlpatterns = [
    path('', Loginview.as_view(), name='loginview'),
    path('administrator/', Administrator.as_view(), name='administrator'),
    path('worker/', Worker.as_view(), name='worker'),
    path('user/', User.as_view(), name='user'),
]
