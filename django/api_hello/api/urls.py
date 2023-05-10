import imp

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (DetailUpdateDeleteFilme, HelloView, ListCreateFilme,
                    UserSignup)

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),

    # User
    path('signup', UserSignup.as_view(), name='signup'),

    # Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API Filmes
    path('filmes', ListCreateFilme.as_view(), name='list-create-filme'),
    path('filmes/<int:pk>', DetailUpdateDeleteFilme.as_view(),
         name='detail-update-delete-filme')
]
