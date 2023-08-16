from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuAPITest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
    def test_getall(self):
        # set up a client to be simelar to API req
        client = APIClient()
        # client login
        client.login(username="testuser",password="testpassword")
        # send GET req
        res = client.get('/restaurant/menu/')
        # get data
        res_data = res.data
        # serialize 
        expected_data = MenuSerializer(Menu.objects.all(),many=True).data
        # assert
        self.assertEqual(res_data,expected_data)

