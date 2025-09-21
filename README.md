# Library API Project

A Django REST API for managing books, user authentication, and posting book reviews.

---

## Setup

1. **Create and activate virtual environment**  
   ```powershell
   .\venv\Scripts\Activate.ps1   # Windows PowerShell
   source venv/bin/activate      # Linux / Mac
Install dependencies

pip install django djangorestframework djangorestframework-simplejwt drf-spectacular pytest pytest-django


Run database migrations

python manage.py migrate


Start development server

python manage.py runserver


Swagger API Documentation:
http://localhost:8000/swagger/

API Endpoints
Authentication

POST auth/register/ – Register a new user

POST auth/login/ – Login and get JWT token

POST auth/refresh/ – Refresh JWT token

Books

GET books/ – List all books

POST books/ – Create book

GET books/{id}/ – Retrieve a single book

PUT books/{id}/ – Update book

DELETE books/{id}/ – Delete book

Reviews

GET/POST books/{id}/reviews/ – List reviews for a book / Create a review
