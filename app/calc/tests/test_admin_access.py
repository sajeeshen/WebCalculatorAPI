from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


CALC_URL = reverse('operation:process')


class AdminCalcTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.admin_user = get_user_model().objects.create_superuser(
            email='myadmin@sajeesh.com',
            password='test123'
        )
        self.token = Token.objects.create(user=self.admin_user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_admin_privilege_operations(self):
        """ Testing if admin users can access admin privilege
            actions
        """
        payload = {'x': 10, 'y': 0, 'action': 'add'}
        res = self.client.post(CALC_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'result': 'success',
            'value': 10
        })
