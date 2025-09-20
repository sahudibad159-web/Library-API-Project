# Library API Project

A simple backend API built with **Django** and **Django REST Framework (DRF)**, featuring JWT authentication, book management, and user reviews.

---

## Features

- JWT-based user authentication (register, login, refresh)
- CRUD operations for books (authenticated users can create, update, delete)
- Add and list reviews for books
- Business logic handled in `services/` folder
- Swagger documentation at `/swagger/`
- Unit tests with pytest

---

## Models

- **User**: Extends Django's `AbstractUser`  
- **Book**: `title`, `author`, `published_date`  
- **Review**: `user`, `book`, `rating (1–5)`, `comment`, includes `username` in response

---

## API Endpoints

### Authentication
- `POST /api/auth/register/` – Register a new user  
- `POST /api/auth/login/` – Login and get JWT token  
- `POST /api/auth/refresh/` – Refresh JWT token  

### Books
- `GET /api/books/` – List all books  
- `POST /api/books/` – Create book (auth required)  
- `GET /api/books/{id}/` – Retrieve a single book  
- `PUT /api/books/{id}/` – Update book (auth required)  
- `DELETE /api/books/{id}/` – Delete book (auth required)  

### Reviews
- `GET /api/books/{id}/reviews/` – List reviews for a book  
- `POST /api/books/{id}/reviews/` – Add review (auth required)  

---

## Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd Library_API_Project/LibraryApiProject
Install dependencies:

pipenv install


Activate virtual environment:

pipenv shell


Apply migrations:

python manage.py migrate


Create a superuser (optional):

python manage.py createsuperuser


Run the development server:

python manage.py runserver


Swagger documentation: http://127.0.0.1:8000/swagger/

Running Tests

Run all unit tests using pytest:

pytest


Tests cover user registration, JWT login, creating/listing books, and creating reviews.
