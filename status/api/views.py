from rest_framework import generics
# from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.views.generic import View

from status.models import Status
from .serializers import StatusSerializer


class StatusListSearchAPIView(APIView):
    permission_classes          = []
    authentication_classes      = []

    def get(self, request, format=None):
        #defined in upper left of webpage: GET /api/status
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #defined in upper left of webpage: adds POST /api/status
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)


class StatusAPIView(generics.ListAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = StatusSerializer #necessary

    def get_queryset(self):
        # /api/status/?q=delete will find all content with keyword delete
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs


class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer #necessary

    # def perform_create(self, serializer):
        # Override method ^
        # eliminates option to choose "author" of post. Author should be logged in user
        # serializer.save(user=self.request.user)


class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer #necessary
    # lookup_field                = 'id' #works also with 'slug'


    # V alternate way instead of using look_upfield
    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)

