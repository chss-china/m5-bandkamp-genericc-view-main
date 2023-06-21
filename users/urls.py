from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework_swagger.views import get_swagger_view
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,

)

    # Acessa o download do schema
   
urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path("users/", views.UserView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
]
