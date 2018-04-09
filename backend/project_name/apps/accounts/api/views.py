from accounts.api.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    search_fields = ('first_name', 'last_name', 'email')
    filter_fields = ('id', 'first_name', 'last_name', 'email')


class UserViewVSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        if pk == 'i':
            return Response(UserSerializer(
                request.user, context={'request': request}).data)
        return super(UserViewSet, self).retrieve(request, pk)
