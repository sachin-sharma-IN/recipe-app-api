"""
Tests for the django admin modifications.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Tests for django admin."""

    def setUp(self):
        """Create user and client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password='testpass123',
        )
        # force_login allows to force the authentication for self.admin_user.
        # Any request we make using client() will be authenticated using this user.
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password='testpass123',
            name='Test User'
        )

    def test_users_list(self):
