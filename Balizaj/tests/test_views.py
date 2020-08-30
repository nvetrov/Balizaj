from django.test import TestCase
from django.test.client import Client
from Balizaj.tests.auth import *
from Balizaj.tests.urls import *
from Balizaj.apps.bali_client.models import *


# Доступность базовых урлов приложений без логина
class ViewsTestCase(TestCase):
    def test_index(self):
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

    def test_client(self):
        response = self.client.get('http://127.0.0.1:8000/client/')
        self.assertEqual(response.status_code, 302)

    def test_bali(self):
        response = self.client.get('http://127.0.0.1:8000/bali/')
        self.assertEqual(response.status_code, 404)


# Доступность урлов приложений для разных групп по логину и паролю и без них
class LoginTestCase(TestCase):
    client = Client()

    def test_login_client(self):
        response = self.client.post('http://127.0.0.1:8000',
                                    {'login': correct_client['login'],
                                     'password': correct_client['password']})
        shop = Shop.objects.create(shop='136')
        shop.save()
        for url in client_url_list:
            response = self.client.get('http://127.0.0.1:8000/client/'+url)
            self.assertEqual(response.status_code, 200)

    def test_login_bali(self):
        response = self.client.post('http://127.0.0.1:8000',
                                    {'login': correct_bali['login'],
                                     'password': correct_bali['password']})
        shop = Shop.objects.create(shop='136')
        shop.save()

        for url in client_url_list:
            response = self.client.get('http://127.0.0.1:8000/client/'+url)
            self.assertEqual(response.status_code, 200)

        for url in bali_url_list:
            response = self.client.get('http://127.0.0.1:8000/bali/'+url)
            self.assertEqual(response.status_code, 200)

    def test_login_incorrect(self):
        response = self.client.post('http://127.0.0.1:8000',
                                    {'login': incorrect_ldap['login'],
                                     'password': incorrect_ldap['password']})
        shop = Shop.objects.create(shop='136')
        shop.save()

        for url in client_url_list:
            response = self.client.get('http://127.0.0.1:8000/client/'+url)
            self.assertEqual(response.status_code, 302)

        for url in bali_url_list:
            response = self.client.get('http://127.0.0.1:8000/bali/'+url)
            self.assertEqual(response.status_code, 302)
