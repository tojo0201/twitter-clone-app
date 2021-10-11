from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('new_account/', views.CreateAccountView.as_view(), name='create_account'),
    path('logout/', views.AccountLogoutView.as_view(), name='logout'),
]
