from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, bmi


urlpatterns = [
    path('', bmi, name='bmi'),
    path('login/', auth_views.login, {'template_name': 'bmi/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/login'}, name='logout'),
    path('signup/', signup, name='signup'),
]
