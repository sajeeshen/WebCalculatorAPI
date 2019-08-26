from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CALC_URL = reverse('operation:process')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicCalcTests(TestCase):
    """ This is the test for checking the public users
        can access the calculator
    """

    def setUp(self):
        self.client = APIClient()

    def test_public_access(self):
        """ Testing public access for the calc api"""
        res = self.client.get(CALC_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_public_calc_post(self):
        """ Testing the public users can pass values to the
            calculator api
        """
        payload = {'x': 10, 'y': 10, 'action': 'Add'}
        res = self.client.post(CALC_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserCalcTests(TestCase):
    """ Testing the authorized users can access the
        calculator api
    """
    def setUp(self):
        self.user = create_user(
            email='test@test.com',
            password='testpass',
            full_name='First Name',
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_private_user_api_access(self):
        """ Testing the private users can access the api link"""
        res = self.client.get(CALC_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_operation_with_invalid_data(self):
        """ Testing one operation with invalid parameters"""
        payload = {'x': '', 'y': '', 'action': 'Add'}
        res = self.client.post(CALC_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_operation_without_action(self):
        """ Testing the operation without the operator"""
        payload = {'x': 10, 'y': 20, 'action': ''}
        res = self.client.post(CALC_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_operation_with_invalid_operation(self):
        """ Testing the calc api with an invalid operator"""
        payload = {'x': 10, 'y': 20, 'action': 'Errr'}
        res = self.client.post(CALC_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_passing_string_parameter(self):
        """ Testing the calc api with an invalid operator"""
        payload = {'x': 'x', 'y': 20, 'action': 'Add'}
        res = self.client.post(CALC_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_valid_inputs(self):
        """ Testing with valid inputs and compare with valid data"""
        payload = {'x': 10, 'y': 20, 'action': 'Add'}
        res = self.client.post(CALC_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'result': 'success',
            'value': 30
        })

    def test_with_zero_division(self):
        """ Testing division by zero"""
        payload = {'x': 10, 'y': 0, 'action': 'divide'}
        res = self.client.post(CALC_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'result': 'success',
            'value': 0
        })

    def test_admin_access_operation(self):
        """ Testing if normal users can access admin privilege
            actions
        """
        payload = {'x': 10, 'y': 0, 'action': 'sqrt'}
        res = self.client.post(CALC_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
