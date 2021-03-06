from django.urls import path
from . import views

app_name = 'Account'

urlpatterns = [
    path('register/<str:type>/',views.register_page,name='register_page'),
    path('login/',views.login_page,name='login_page'),
    path('logout/',views.logout_page,name='logout_page'),
]