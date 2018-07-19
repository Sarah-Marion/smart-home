from django.test import TestCase
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .views import LoginUserView

# Create your tests here.
class LoginUser(APITestCase):
    # urlpatterns = [
    #     path((r'^',include(('restLogin.urls','restLogin'),namespace="rest-login")),
    #     ]

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        # url = reverse('account-list')
        data = {'name': 'Washere'}
        response = self.client.post( data, format='json')
        self.assertTrue(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Account.objects.count(), 1)
        # self.assertEqual(Account.objects.get().name, 'Washere')