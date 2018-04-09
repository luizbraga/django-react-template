from django.urls import path
from accounts.api.views import UserViewSet
from accounts.api.views import UserViewVSet
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('list/', UserViewSet.as_view({'get': 'list'}), name='user_view'),
    path('users/<pk>/', UserViewVSet.as_view(
        {'get': 'retrieve'}), name='user_vview'),
    path('obtain-token/', obtain_auth_token, name='auth_token'),
]
