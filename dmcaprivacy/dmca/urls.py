from django.urls import path
from .views import Index


urlpatterns = [
    # path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    path('', Index.as_view(), name='index'),
]
