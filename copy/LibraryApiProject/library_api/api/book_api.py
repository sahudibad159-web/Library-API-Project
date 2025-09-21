from django.urls import path
from ..views import BookListCreateView, BookDetailView

book_urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:book_id>/", BookDetailView.as_view(), name="book-detail"),
]
