
import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from orderapi.serializers import BookOrderSerializer
from orderapi.models import BookOrder

class BookOrderViewsetTestCase(APITestCase):

    def setup(self):

        self.user = User.objects.create_user(username="myuser", password="password")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token" + self.token.key)