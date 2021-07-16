from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('register_page/', register_page, name='register_page'),
    path('register/', register, name='register'),
    
    path('login_page/', login_page, name='login_page'),
    path('login/', login, name='login'),
    
    path('profile_page/', profile_page, name='profile_page'),
    path('update_profile/', update_profile, name='update_profile'),
    
    path('update_education/', update_education, name='update_education'),
    path('remove_education/<int:pk>/', remove_education, name='remove_education'),

    path('update_language/', update_language, name='update_language'),
    path('remove_language/<int:pk>/', remove_language, name='remove_language'),
    
    path('logout/', logout, name='logout'),
]