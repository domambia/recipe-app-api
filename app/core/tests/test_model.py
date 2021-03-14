from django.test import TestCase 
from django.contrib.auth import get_user_model


class ModelTests(TestCase):


    def test_create_user_successful(self):
        """Test creating user using email succesful"""
        email  = "test@test.com"
        password = "testpass123"
        user  = get_user_model().objects.create_user(email = email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    
    def test_new_user_email_is_normalized(self):
        """Test the email of new user is normalized"""
        email = "test@EMAIL.COM"
        user =  get_user_model().objects.create_user(email = email, password= 'testpass')

        self.assertEqual(user.email, email.lower());

    
    def test_new_user_invalid_email(self):
        """Test that new user provides invalid email address"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, password="testpass")

    
    def test_create_new_super_user(self):
        """Test creating a new super user """

        user  = get_user_model().objects.create_superuser(
            email  =  "test@test.com",
            password = "pass123212"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
            