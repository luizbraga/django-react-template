from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('api/accounts/', include(
        ('accounts.api.urls', 'accounts'), namespace='accounts')),
    path('api-auth/', include(
        ('rest_framework.urls', 'rest_framework'), namespace='rest_framework')
    ),
    path('admin/', admin.site.urls),
]
