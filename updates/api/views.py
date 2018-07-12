

from updates.models import Update as UpdateModel

#recommended way V if youre building a public app. do not separate out and create indivual views for each method.

class UpdateModelDetailAPIView():
    def get(self, request, *args, **kwargs):
        # handles retrieve method

        return #json

    def post(self, request, *args, **kwargs):
        # handles create method

        return #json

    def put(self, request, *args, **kwargs):
        # handles update method

        return #json

    def delete(self, request, *args, **kwargs):
        # handles delete method

        return #json


class UpdateModelListAPIView():
    def get(self, request, *args, **kwargs):
        # handles retrieve method

        return #json