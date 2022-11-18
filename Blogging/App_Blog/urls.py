
from django.urls import path,include
from . import views
app_name='App_Blog'

urlpatterns = [
   path('',views.BlogList.as_view(),name='blog_list'),
   path('write/',views.CreateBlog.as_view(),name='create_blog'),
   path('details/<str:slug>',views.blog_details,name='blog_details'),
   path('liked/<pk>',views.liked,name='liked_post'),
   path('disliked/<pk>',views.unliked,name='unliked_post'),
   path('my-blog/',views.MyBlogs.as_view(),name='my_blogs'),
   path('edit-blog/<pk>',views.UpdateBlog.as_view(),name='edit_blog'),


] 