from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationTests(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.region = 'Test Region'

    def test_user_registration(self):
        response = self.client.post(reverse('registration'), {
            'username': self.username,
            'password1': self.password,
            'password2': self.password,
            'region': self.region,
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username=self.username).exists())

    def test_user_login(self):
        self.client.post(reverse('registration'), {
            'username': self.username,
            'password1': self.password,
            'password2': self.password,
            'region': self.region,
        })
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login

    def test_dashboard_access(self):
        self.client.post(reverse('registration'), {
            'username': self.username,
            'password1': self.password,
            'password2': self.password,
            'region': self.region,
        })
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)  # Dashboard should be accessible
        self.assertContains(response, self.region)  # Check if region is displayed on the dashboard