import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from api.models import User, Book

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

@pytest.mark.django_db
def test_create_book_authenticated():
    user = User.objects.create_user(username="test", password="pass123")
    client = APIClient()
    token = client.post(reverse("login"), {"username": "test", "password": "pass123"}).data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    response = client.post(reverse("book-list-create"), {"title": "Book 1", "author": "Author", "published_date": "2023-01-01"})
    assert response.status_code == 201
