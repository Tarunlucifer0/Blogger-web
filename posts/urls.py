from django.urls import path
from . import views

app_name= 'posts'
urlpatterns = [
    path('', views.posts_list, name="list"), #this name will use in html file
    path('new-post/', views.new_post, name="new_post"), #this name will use in html file
    path('<slug:slug>', views.post_page, name='page'), #this name will use in html file
]
