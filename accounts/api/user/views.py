from django.contrib.auth import  get_user_model
from rest_framework import generics, permissions
from accounts.api.permissions import AnonPermissionOnly


from status.api.serializers import StatusInLineUserSerializer
from status.models import Status

from .serializers import UserDetailSerializer

User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    # permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset            =  User.objects.filter(is_active=True)
    serializer_class    = UserDetailSerializer
    lookup_field        = 'username'

    def get_serializer_context(self):
        return {'request': self.request}

class UserStatusAPIView(generics.ListAPIView):
    serializer_class    = StatusInLineUserSerializer

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)