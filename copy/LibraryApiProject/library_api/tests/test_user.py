import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from library_api.models import User

@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    response = client.post(reverse("register"), {"username": "test", "password": "pass123"})
    assert response.status_code == 201

@pytest.mark.django_db
def test_jwt_login():
    user = User.objects.create_user(username="test", password="pass123")
    client = APIClient()
    response = client.post(reverse("login"), {"username": "test", "password": "pass123"})
    assert "access" in response.data
