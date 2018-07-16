import json
from django.views.generic import View
from django.http import HttpResponse

from cfeapi.mixins import HttpResponseMixin

from updates.forms import UpdateModelForm
from updates.models import Update as UpdateModel
from .mixins import CSRFExemptMixin

from.utils import is_json


class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin,View):
    #recommended way V if youre building a public app. do not separate out and create indivual views for each method.
    '''
        retrieve, update, Delete ---> object
        '''

    is_json = True

    def get_object(self, id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj = None

        '''
            Below handles a Does Not Exist Exception too
        '''

        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, id, *args, **kwargs):
        # handles retrieve method
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        # handles create method
        json_data = json.dumps({"message": "Not allowed, Please use the /api/updates/ endpoint."})
        return self.render_to_response(json_data, status=403)

    def put(self, request, id, *args, **kwargs):
        # handles update method
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Invalid data sent"})
            return self.render_to_response(error_data, status=400)

        new_data = json.loads(request.body)
        print(new_data['content'])
        json_data = json.dumps({"message": "something else"})
        return self.render_to_response(json_data)

    def delete(self, request, id, *args, **kwargs):
        # handles delete method
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)

        json_data = json.dumps({"message": "something else"})
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
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Invalid data sent"})
            return self.render_to_response(error_data, status=400)
        data = json.loads(request.body)
        form = UpdateModelForm(data)
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
