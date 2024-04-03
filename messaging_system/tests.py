from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Message


class MessageTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.url_messages = '/api/messages/'
        self.url_unread_messages = '/api/unread-messages/'

    def test_list_create_messages(self):
        Message.objects.create(sender=self.user, receiver=self.user, message='Test message 1', subject='Subject 1')
        Message.objects.create(sender=self.user, receiver=self.user, message='Test message 2', subject='Subject 2')

        response = self.client.get(self.url_messages)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        data = {'message': 'New message', 'subject': 'New Subject', 'receiver': self.user.id}
        response = self.client.post(self.url_messages, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Message.objects.count(), 3)
        self.assertEqual(Message.objects.last().message, 'New message')

    def test_list_unread_messages(self):
        Message.objects.create(sender=self.user, receiver=self.user, message='Read message', is_read=True)
        Message.objects.create(sender=self.user, receiver=self.user, message='Unread message', is_read=False)

        response = self.client.get(self.url_unread_messages)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_delete_message(self):
        message = Message.objects.create(sender=self.user, receiver=self.user, message='Test message')

        response = self.client.delete(f'/api/messages/{message.id}/')
        self.assertEqual(response.status_code, 204)

        response = self.client.get(f'/api/messages/{message.id}/')
        self.assertEqual(response.status_code, 404)