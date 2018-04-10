from accounts.api.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response

User = get_user_model()


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    search_fields = ('username', 'email', 'is_active')
    filter_fields = ('email', 'is_active')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        if pk == 'i':
            return Response(UserSerializer(
                request.user, context={'request': request}).data)
        return super(UserViewSet, self).retrieve(request, pk)
