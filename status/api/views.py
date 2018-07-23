from rest_framework import generics, mixins
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


# CreateModelMixin --- handles POST method
# UpdateModelMixin --- handles PUT method
# DestroyModelMixin -- DELETE method


class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
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

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        #comes from model mixin

    # def perform_create(self, serializer):
        # Override method ^, eliminates option to choose "author" of post. Author should be logged in user
        # serializer.save(user=self.request.user)

class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer #necessary




class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer #necessary

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        #comes from model mixin

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        #comes from model mixin

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



'''
class StatusUpdateAPIView(generics.UpdateAPIView): #updateing to create list api view
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer #necessary


class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer #necessary
'''
