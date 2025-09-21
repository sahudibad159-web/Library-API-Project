from library_api.models import Book

def list_books():
    return Book.objects.all()

def create_book(data):
    return Book.objects.create(**data)

def get_book(book_id):
    return Book.objects.get(id=book_id)

# services/book_service.py
def update_book(book, data):
    for attr, value in data.items():
        setattr(book, attr, value)
    book.save()
    return book

def delete_book(book):
    book.delete()
