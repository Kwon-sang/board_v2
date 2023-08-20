from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.UserCreateView.as_view(), name='signup'),

]