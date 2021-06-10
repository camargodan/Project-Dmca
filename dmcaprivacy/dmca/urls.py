from django.urls import path
from .views import Loginview, Administrator, Worker, Client, UserEditView, ManageUsers
from django.contrib.auth import get_user_model

User = get_user_model()


urlpatterns = [
    path('', Loginview.as_view(), name='loginview'),
    path('administrator/', Administrator.as_view(), name='administrator'),
    path('worker/', Worker.as_view(), name='worker'),
    path('client/', Client.as_view(), name='client'),
    path('edit_user/<slug:slug>/', UserEditView.as_view(), name='edit_user'),
    path('manage_users/', ManageUsers.as_view(), name='manage_users')

]
