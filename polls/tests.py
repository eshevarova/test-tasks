import datetime
import json

from django.utils import timezone
from django.urls import reverse
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Question



class QuestionTests(APITestCase):
    time = timezone.now()
    data_poll = {'question_text': 'How are you?', "pub_date": str(timezone.now()), "choice_set": []}
    

    def test_create_object(self):
        client = APIClient()
        response = client.post(reverse('polls:create'), data=json.dumps(self.data_poll), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(len(Question.objects.all()), 1)

    def test_get_object(self):
        client = APIClient()
        response = client.get(reverse('polls:create'))
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
