from django.urls import path
from . import views

urlpatterns = [
    path('postlist/', views.post_list, name='post_list'),
    path('postdetail/<int:id>/',views.post_detail, name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('postedit/<int:id>/',views.post_edit,name='post_edit'),
]