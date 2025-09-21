# Library API Project

A Django REST API for managing books, user authentication, and posting book reviews.

---

## Setup

1. **Create a virtual environment and activate it**

   **Windows (PowerShell):**
   ```powershell
   .\venv\Scripts\Activate.ps1
Windows (cmd):

cmd
Copy code
venv\Scripts\activate
Linux / Mac:

bash
Copy code
source venv/bin/activate
Install dependencies

bash
Copy code
pip install django djangorestframework djangorestframework-simplejwt drf-spectacular pytest pytest-django
Run database migrations

bash
Copy code
python manage.py migrate
Start the development server

bash
Copy code
python manage.py runserver
Swagger API Documentation

bash
Copy code
http://localhost:8000/swagger/
API Endpoints
Authentication
Method	Endpoint	Description
POST	auth/register/	Register a new user
POST	auth/login/	Login and get JWT token
POST	auth/refresh/	Refresh JWT token

Books
Method	Endpoint	Description
GET	books/	List all books
POST	books/	Create a new book
GET	books/{id}/	Retrieve a single book
PUT	books/{id}/	Update a book
DELETE	books/{id}/	Delete a book

Reviews
Method	Endpoint	Description
GET	books/{id}/reviews/	List reviews for a book
POST	books/{id}/reviews/	Create a review for a book

Project Structure
markdown
Copy code
LibraryAPIProject/
│
├─ manage.py
├─ db.sqlite3
├─ Pipfile
├─ Pipfile.lock
├─ pytest.ini
│
├─ library_api/
│   ├─ __init__.py
│   ├─ admin.py
│   ├─ apps.py
│   ├─ models.py
│   ├─ views.py
│   ├─ urls.py
│   ├─ tests.py
│   │
│   ├─ api/
│   │   ├─ __init__.py
│   │   ├─ user_api.py
│   │   ├─ book_api.py
│   │   └─ review_api.py
│   │
│   ├─ serializer/
│   │   ├─ __init__.py
│   │   ├─ user_serializer.py
│   │   ├─ book_serializer.py
│   │   └─ review_serializer.py
│   │
│   ├─ services/
│   │   ├─ __init__.py
│   │   ├─ user_service.py
│   │   ├─ book_service.py
│   │   └─ review_service.py
│   │
│   └─ migrations/
│       ├─ __init__.py
│       └─ 0001_initial.py
│
└─ LibraryApi/
    ├─ __init__.py
    ├─ asgi.py
    ├─ settings.py
    ├─ urls.py
    └─ wsgi.py# Library-API-Project
