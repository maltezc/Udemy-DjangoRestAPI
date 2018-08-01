import datetime

from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse #<-- similar to regular django reverse #another version is django hosts

from status.api.serializers import StatusInLineUserSerializer

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    uri             = serializers.SerializerMethodField(read_only=True)
    status          = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'status', # same as model name --> user's ownership of that model name
        ]

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-user:detail", kwargs={"username": obj.username}, request=request)

    def get_status(self, obj):
        request = self.context.get('request')
        limit = 10
        if request:
            limit_query = request.GET.get('limit')
            try:
                limit = int(limit_query)
            except:
                pass
        qs = obj.status_set.all().order_by("-timestamp") # [:10]
        data = {
            'uri': self.get_uri(obj) + "status/",
            'last': StatusInLineUserSerializer(qs.first(), context={'request': request}).data,
            'recent': StatusInLineUserSerializer(qs[:limit], many=True, context={'request': request}).data
        }
        return data
