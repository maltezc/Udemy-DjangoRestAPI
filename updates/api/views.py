import json
from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel

from .mixins import CSRFExemptMixin

#recommended way V if youre building a public app. do not separate out and create indivual views for each method.
class UpdateModelDetailAPIView(CSRFExemptMixin ,View):
    '''
    retrieve, update, Delete ---> object
    '''
    def get(self, request, id, *args, **kwargs):
        # handles retrieve method
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()

        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        # handles create method

        return HttpResponse({}, content_type='application/json')

    def put(self, request, *args, **kwargs):
        # handles update method

        return HttpResponse({}, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        # handles delete method

        return HttpResponse({}, content_type='application/json')


class UpdateModelListAPIView( CSRFExemptMixin, View):
    '''
    List View
    Create View
    '''
    def get(self, request, *args, **kwargs):
        # handles retrieve method
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        # handles create method
        data = json.dumps({'message': 'Unknown Data'})
        return HttpResponse(data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        # handles delete method
        data = json.dumps({'message': 'You cannot delete an entire list'})

        return HttpResponse(data, content_type='application/json')
