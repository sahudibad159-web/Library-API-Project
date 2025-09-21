from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from library_api.models import Book, Review
from library_api.serializer import (
    UserSerializer,
    BookSerializer,
    ReviewSerializer,
)
from library_api.services import book_service


# --- Registration ---
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# --- Book List / Create ---
class BookListCreateView(APIView):
    permission_classes = [IsAuthenticated]  # Requires JWT

    def get(self, request):
        books = book_service.list_books()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book_service.create_book(serializer.validated_data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# --- Book Detail ---
class BookDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, book_id):
        book = book_service.get_book(book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, book_id):
        book = book_service.get_book(book_id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, book_id):
        book = book_service.get_book(book_id)
        book.delete()
        return Response(status=204)


# --- Review List / Create ---
class ReviewListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, book_id=book_id)  # assign automatically
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
