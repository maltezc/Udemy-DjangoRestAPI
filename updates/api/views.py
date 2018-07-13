import json
from django.views.generic import View
from django.http import HttpResponse

from cfeapi.mixins import HttpResponseMixin

from updates.forms import UpdateModelForm
from updates.models import Update as UpdateModel
from .mixins import CSRFExemptMixin

#recommended way V if youre building a public app. do not separate out and create indivual views for each method.
class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin,View):
    '''
    retrieve, update, Delete ---> object
    '''

    is_json = True

    def get(self, request, id, *args, **kwargs):
        # handles retrieve method
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        # handles create method
        json_data = json.dumps({"message": "Not allowed, Please use the /api/updates/ endpoint."})
        return self.render_to_response(json_data, status=403)

    def put(self, request, *args, **kwargs):
        # handles update method
        json_data = {}

        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        # handles delete method
        json_data = {}
        self.render_to_response(json_data, status=403)


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    '''
    List View
    Create View
    check wikipedia for status codes
    '''

    is_json = True


    def get(self, request, *args, **kwargs):
        # handles retrieve method
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        # handles create method
        # print(request.POST)
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = {"message": "Not Allowed"}
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        # handles delete method
        data = json.dumps({'message': 'You cannot delete an entire list'})
        status_code = 403 # not allowed
        return self.render_to_response(data, status=403)
