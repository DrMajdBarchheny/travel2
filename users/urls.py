from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,

)
from . import views


urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', views.getUserProfile, name='getUserProfile'),
    path('', views.getUsersProfile, name='getUsersProfile'),
    path('register/',views.registerUser , name='registerUser') ,
]
