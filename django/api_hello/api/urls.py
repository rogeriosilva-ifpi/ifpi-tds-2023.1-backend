from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import (DetailUpdateDeleteFilmeView, HelloView,
                    ListCreateFilmeView, SignupView)

urlpatterns = [
    path('hello/', HelloView.as_view(), name='Hello end'),

    # API Filmes
    path('filmes', ListCreateFilmeView.as_view()),
    path('filmes/<int:pk>', DetailUpdateDeleteFilmeView.as_view()),

    # Signup
    path('signup', SignupView.as_view()),

    # Signin (access-token, refresh-token)
    path('token', TokenObtainPairView.as_view())
]
