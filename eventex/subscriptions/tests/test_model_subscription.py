from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Mateus',
            cpf=32783355892,
            email='mateusflavio@gmail.com',
            phone='16-992966600'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        self.assertIsInstance(self.obj.create_at, datetime)

    def test_str(self):
        self.assertEqual('Mateus', str(self.obj))