from django.urls import path
from . import views

urlpatterns = [
    path('function/',views.function,name='function'),
    path('login/',views.login,name='login')
]
