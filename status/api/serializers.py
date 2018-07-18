from rest_framework import serializers

from status.models import Status

'''
**serializers turn data into JSON data**
JSON -- JavaScript Object Notation

Serializers --> JSON
Serializers --> validate Data


'''
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

