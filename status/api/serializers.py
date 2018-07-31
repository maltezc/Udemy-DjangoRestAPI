from rest_framework import serializers

from accounts.api.serializers import UserPublicSerializer
from status.models import Status

'''
**serializers turn data into JSON data**
JSON -- JavaScript Object Notation

Serializers --> JSON
Serializers --> validate Data
'''


class StatusSerializer(serializers.ModelSerializer):
    uri         = serializers.SerializerMethodField(read_only=True)
    user        = UserPublicSerializer(read_only=True)
    class Meta:
        model = Status
        fields = [
            'uri',
            'id', # ?
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user'] #GET calls only. change users anymore

    def get_uri(self,obj):
        return "api/status/{id}/".format(id=obj.id)

    #field level validation
    # def validate_<fieldname>(self, value):
    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError("This is way too long")
    #     return value

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("content or image is required")
        return data

