from django.urls import path
from accounts.api.views import UserViewSet

urlpatterns = [
    path('list/', UserViewSet, name='user_view'),
]
