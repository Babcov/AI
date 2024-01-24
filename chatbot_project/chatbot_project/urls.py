from django.urls import path
from chatbot import views

urlpatterns = [
       path('', views.home, name='home'),
       path('add/', views.add_message, name='add_message'),
   ]
