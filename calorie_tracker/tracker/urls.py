from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_food/', views.add_food, name='add_food'),
    path('set_goal/', views.set_goal, name='set_goal'),
]
