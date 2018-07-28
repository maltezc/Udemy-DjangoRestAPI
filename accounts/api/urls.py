from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token # would usually go in the accounts app
# ^ passes through user's password and username for authentication when required

from .views import AuthAPIView, RegisterAPIView


# if django 2.0, this looks different V
urlpatterns = [
    url(r'^$', AuthAPIView.as_view()),
    url(r'^register/$', RegisterAPIView.as_view()),
    url(r'^jwt/$', obtain_jwt_token),
    url(r'^jwt/refresh/$', refresh_jwt_token),
]
