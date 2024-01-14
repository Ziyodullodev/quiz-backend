from django.conf.urls.static import static
from utils.swagger import schema_view
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # path('rosetta/', include('rosetta.urls')),
    path('admin-p/', admin.site.urls),
]

urlpatterns += [
    path('docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/user/', include('apps.users.urls')),
    path('api/quiz/', include('apps.quiz.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)