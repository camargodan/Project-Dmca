from django.urls import path
from .views import LoginView, Administrator, Worker, Client, UserEditView, ManageUsers, ManagePlans, CreatePlan
from django.contrib.auth import get_user_model


User = get_user_model()

urlpatterns = [
    path('', LoginView.as_view(), name='loginview'),
    path('administrator/', Administrator.as_view(), name='administrator'),
    path('worker/', Worker.as_view(), name='worker'),
    path('client/', Client.as_view(), name='client'),
    path('edit_user/<slug:slug>/', UserEditView.as_view(), name='edit_user'),
    path('manage_user', ManageUsers.as_view(), name='manage_users'),
    path('manage_plan', ManagePlans.as_view(), name='manage_plans'),
    path('plans/add', CreatePlan.as_view(), name='create_plan'),

]

