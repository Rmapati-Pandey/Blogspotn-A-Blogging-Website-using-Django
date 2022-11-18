
from django.urls import path,include
from . import views

app_name='App_Login'  
urlpatterns = [
   path('signup/',views.signup,name='signup'),
   path('signin/',views.login_page, name='signin'),
   path('logout/',views.logout_user,name='logout'),
   path('profile/',views.profile,name='profile'),
   path('update-profile/',views.UpdateProfile,name='updateprofile'),
   path('password/',views.UpdatePassword,name='updatepassword'),
   path('updateprofilepic/',views.UpdateProfilePic,name='updateprofilepic')
]
