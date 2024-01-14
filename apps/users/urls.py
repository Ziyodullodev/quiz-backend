from .views import LoginAPIView, RegisterAPIView, UpdateAPIView
from django.urls import path


urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("update/", UpdateAPIView.as_view(), name="update"),

]