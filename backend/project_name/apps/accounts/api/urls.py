from accounts.api.views import UserList
from accounts.api.views import UserViewSet
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('list/', UserList.as_view({'get': 'list'}), name='user_list'),
    path('users/<pk>/', UserViewSet.as_view(
        {'get': 'retrieve'}), name='user_view'),
    path('obtain-token/', obtain_auth_token, name='auth_token'),
]
