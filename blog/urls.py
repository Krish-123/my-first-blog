from django.urls import path
from . import views

urlpatterns = [
    path('postlist/', views.post_list, name='post_list'),
]