from . import views
from django.urls import path


urlpatterns = [

    path('',views.home,name='index'),
    path('login/',views.login,name='login'),
    path('login/login',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('register/login',views.register,name='register'),
    path('register/register',views.register,name='register'),
    path('form/',views.form,name='form'),
    path('form/result/',views.result,name='result'),
    path('logout/',views.logout,name='logout'),
    path('form/result/logout',views.logout,name='logout')
]