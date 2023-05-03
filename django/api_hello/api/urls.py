from django.urls import path

from .views import HelloView

urlpatters = [
    path('hello/', HelloView.as_view(), name='hello')
]
