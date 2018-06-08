from django.urls import path
from django.urls import include
from django.conf import settings
from django.views.generic import TemplateView

from core.site import admin


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('api/accounts/', include('accounts.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
