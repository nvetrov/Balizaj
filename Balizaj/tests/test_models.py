from django.test import TestCase
from Balizaj.apps.bali_client.models import *
from Balizaj.apps.bali_client.mag_number_auth import Auth
from Balizaj.tests.auth import *  # импорт словарей с лдап и пасс


# Поведение класса ответственного за соединение с AD в зависимости от корректности данных
class AuthTestCase(TestCase):

    def test_connect_incorrect_pass(self):
        user = Auth(login=incorrect_pass['login'], password=incorrect_pass['password'])
        self.assertEqual(user.user_valid(), False)

    def test_connect_incorrect_ldap(self):
        user = Auth(login=incorrect_ldap['login'], password=incorrect_ldap['password'])
        self.assertEqual(user.user_valid(), False)

    def test_connect_empty_ldap(self):
        user = Auth(login=empty_ldap['login'], password=empty_ldap['password'])
        self.assertEqual(user.user_valid(), False)

    def test_connect_empty_pass(self):
        user = Auth(login=empty_pass['login'], password=empty_pass['password'])
        self.assertEqual(user.user_valid(), False)

    def test_connect_correct_ldapa(self):
        user = Auth(login=correct_ldapa['login'], password=correct_ldapa['password'])
        self.assertEqual(user.user_valid(), False)

    def test_connect_client(self):
        user = Auth(login=correct_client['login'], password=correct_client['password'])
        self.assertEqual(user.shop_number, '136')
        self.assertEqual(user.shop_verbose, 'Магазин Санкт-Петербург (Петергофское)')
        self.assertEqual(user.group, 'client')
        self.assertEqual(user.user_valid(), True)

    def test_connect_bali(self):
        user = Auth(login=correct_bali['login'], password=correct_bali['password'])
        self.assertEqual(user.shop_number, '136')
        self.assertEqual(user.shop_verbose, 'Магазин Санкт-Петербург (Петергофское)')
        self.assertEqual(user.group, 'bali')
        self.assertEqual(user.user_valid(), True)


# Поведение модели магазина в зависимости от типа данных передаваемых на вход
class ShopTestCase(TestCase):
    def setUp(self):
        Shop.objects.create(shop=136)
        Shop.objects.create(shop='042')

    def test_shop(self):
        correct1 = Shop.objects.get(shop='136')
        correct1_1 = Shop.objects.get(shop=136)
        correct2 = Shop.objects.get(shop='42')
        correct2_1 = Shop.objects.get(shop=42)
        self.assertEqual(correct1.shop, 136)
        self.assertEqual(correct1_1.shop, 136)
        self.assertEqual(correct2.shop, 42)
        self.assertEqual(correct2_1.shop, 42)
