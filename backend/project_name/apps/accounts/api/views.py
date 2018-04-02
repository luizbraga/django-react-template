from django.contrib.auth.models import User
from rest_framework import viewsets
from accounts.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    search_fields = ('first_name', 'last_name', 'email')
    filter_fields = ('id', 'first_name', 'last_name', 'email')
