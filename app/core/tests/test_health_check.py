""" Test for the health check API """

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckApiTests(TestCase):
    """ Test module for health check API """

    def setUp(self):
        self.client = APIClient()

    def test_health_check(self):
        """ Test health check API """
        url = reverse('health-check')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
