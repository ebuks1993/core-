from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='main_home'),
    path('post/<int:id>',views.post_detail,name='postdetail'),
    path('createpost/',views.createpost,name='createpost'),
    path('register/',views.register,name='register'),
    
]