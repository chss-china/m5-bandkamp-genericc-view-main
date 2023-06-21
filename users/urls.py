from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework_swagger.views import get_swagger_view


    # Acessa o download do schema
   
urlpatterns = [
   
    path("users/", views.UserView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    
    
]
