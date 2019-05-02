from django.urls import path
from . import views

urlpatterns = [
    path('postlist/', views.post_list, name='post_list'),
    path('postdetail/<int:id>/',views.post_detail, name='post_detail')
]