from urllib import response

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class ListCreateFilmeTestCase(TestCase):

    def signup(self):
        # Signup
        singup_data = {"username": "rogerio410",
                       "password": "123456", "email": "rogerio410_@gmail.com"}
        response = self.client.post(reverse('signup'), singup_data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def get_token(self):
        # Login
        login_data = {"username": "rogerio410", "password": "123456"}
        response = self.client.post(reverse('token_obtain_pair'), login_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        access_token = response.data['access']
        return f'Bearer {access_token}'

    def setUp(self):
        self.client = APIClient()
        self.signup()
        self.authorization_header = self.get_token()

    def test_deve_lista_filmes(self):
        url = reverse('list-create-filme')
        response = self.client.get(
            url, HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 0)
