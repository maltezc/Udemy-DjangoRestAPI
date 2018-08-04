from django.urls import reverse
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model


from status.models import Status
User = get_user_model()


class StatusAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='cfe', email='hello@cfe.com')
        user.set_password("yeahhhcfe")
        user.save()

        status_obj = Status.objects.create(user=user, content='Hello There!')

    def _test_statuses(self):
        self.assertEqual(Status.objects.count(), 1)

    def status_user_token(self):
        auth_url = api_reverse('api-auth:login')
        auth_data = {
            'username': 'cfe',
            'password': 'yeahhhcfe',
        }
        auth_response = self.client.post(auth_url, auth_data, format='json')
        token = auth_response.data.get("token", 0)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

    def create_item(self):
        self.status_user_token() #calls def status usertoken above instead of having to repeat code
        url = api_reverse('api-status:list')
        data = {
            'content': 'some cool test content'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Status.objects.count(), 2)
        return response.data

    def test_status_create(self):
        data = self.create_item()
        data_id = data.get("id")
        rud_url = api_reverse('api-status:detail', kwargs={"id": data_id})
        rud_data = {
            'content': 'another new content'
        }

        '''
        get method / retrieve
        '''
        get_response = self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)



    def test_status_update(self):
        data = self.create_item()
        data_id = data.get("id")
        rud_url = api_reverse('api-status:detail', kwargs={"id": data_id})
        rud_data = {
            'content': 'another new content'
        }

        '''
        put / update
        '''
        put_response = self.client.put(rud_url, rud_data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        rud_response_data = put_response.data
        self.assertEqual(rud_response_data['content'], rud_data['content'])

    def test_status_delete(self):
        data = self.create_item()
        data_id = data.get("id")
        rud_url = api_reverse('api-status:detail', kwargs={"id": data_id})
        rud_data = {
            'content': 'another new content'
        }

        '''
        delete method 
        '''
        del_response = self.client.delete(rud_url, format='json')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)

        '''
        Not Found 
        '''
        get_response = self.client.delete(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)


    def test_status_no_token_create(self):
        url = api_reverse('api-status:list')
        data = {
            'content': 'some cool test content'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

