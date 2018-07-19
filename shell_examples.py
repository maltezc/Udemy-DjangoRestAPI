from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parseres import JSONParser

from status.api.serializers import StatusSerializer
from status.models import Status


'''
Serialize a single object
'''
obj = Status.objects.first()
serializer = StatusSerializer(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)


'''
Serialize a queryset
'''
qs = Status.objects.all()
serializer2 = StatusSerializer(qs, many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data)

stream2 = BytesIO(json_data2)
data2 = JSONParser.parse(stream2)
print(data2)



'''
Create obj
'''
data = {'user': 1}
serializer = StatusSerializer(data=data)
serializer.is_valid()
serializer.save()


# if serializer.is_valid():
#     serializer.save()


'''
Update obj
'''
obj = Status.objects.first()
data = {'content': 'some new content', "user": 1}
update_serializer = StatusSerializer(obj, data=data)
update_serializer.is_valid()
update_serializer.save()
# update_serializer.errors <-- will show errors in shell


'''
Delete obj
'''

data = {'user': 1, "content":"please delete me"}
create_obj_serializer = StatusSerializer(data=data)
create_obj_serializer.is_valid()
create_obj = create_obj_serializer.save() #returns instance of object
print(create_obj)


# data = {'id': 6}
obj = Status.objects.last()
get_data_serializer = StatusSerializer(obj)
# update_serializer.is_valid()
# update_serializer.save()
print(obj.delete())


#serializers help change data
