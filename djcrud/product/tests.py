from datetime import *
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Category, Product
from django.test import Client
from django.contrib.auth import login

class UserTestCase(TestCase):
    def setUp(self):

        User.objects.create(username='testuser', password='12345')



    def test_user_auth(self):
        """ User is Automatically login when they are signup so need to logout"""
        user = User.objects.get(username='testuser')
        login(,user)
        # response = self.client.get('login/')
        # self.assertEquals(user, response.status_code, 200)

        # # cat_name = Category.objects.get(cat_name="cat_test_4")
        # c = Client()
        # logged_in = c.login(username='testuser', password='12345')
        # self.assertEquals(user,logged_in, response.status_code, 200)
        # # self.assertEqual(cat_name.cat_name, "cat_test_4")


class CategoryTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username ='testuser')
        Category.objects.create(cat_name='cat_test_4', created=datetime.now(), updated=datetime.now(), user=user)

    def test_cat_operations(self):
        """Creating Category using TestUser"""
        cat_name = Category.objects.get(cat_name="cat_test_4")
        self.assertEqual(cat_name.cat_name, "cat_test_4")


class ProductTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser')
        category = Category.objects.create(cat_name='cat_test_4', created=datetime.now(), updated=datetime.now(),
                                           user=user)
        Product.objects.create(product_name='Aaloo', category=category, created=datetime.now(), updated=datetime.now(),
                               user=user)

    def test_cat_store(self):
        """Creating Product Using test user"""
        name = Product.objects.get(product_name="Aaloo")
        self.assertEqual(name.product_name, "Aaloo")
