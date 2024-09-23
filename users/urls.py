from django.urls import path
from . import views

app_name= 'users'
urlpatterns = [
    path('register/', views.register_view, name='register'), #this name will use in html file
    path('login/', views.login_view, name='login'), #this name will use in html file
    path('logout/', views.logout_view, name='logout')
    
]
