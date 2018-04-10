from django.urls import path
from django.urls import include
from core.site import admin

urlpatterns = [
    path('api/accounts/', include('accounts.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.urls),
]
