from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('delete/<int:post_id>/',views.delete, name='delete'),
    
    #          <int:post_id>--------(type of data : unique url) specifies the post
    path('edit/<int:post_id>/',views.edit ),
    path('likes/<int:post_id>/',views.likes),
]