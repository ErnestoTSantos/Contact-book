from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter
from rest_framework_swagger.views import get_swagger_view

from gize.apps.contacts.views import ContactViewSet, PhoneTypeView
from gize.apps.user.views import UserInformationViewSet, login_user

api_router_v1 = SimpleRouter()
api_router_v1.register("contacts", ContactViewSet, basename="contact")
api_router_v1.register("users", UserInformationViewSet, basename="users")

schema_view = get_schema_view(
   openapi.Info(
      title="API's",
      default_version='v1',
      description="Contact book informations",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="email"),
      license=openapi.License(name="License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_router_v1.urls)),
    path('api/v1/login-user/', login_user, name="login-user"),
    path('api/v1/phone-type/', PhoneTypeView.as_view(), name="phone-type"),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
]
