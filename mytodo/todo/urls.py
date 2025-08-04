from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('toggle/<int:item_id>/', views.toggle_complete, name='toggle_complete'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
