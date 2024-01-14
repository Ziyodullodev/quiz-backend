from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="QUiz backend swagger",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="testmail@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)