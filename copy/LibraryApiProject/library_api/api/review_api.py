from django.urls import path
from ..views import ReviewListCreateView

review_urlpatterns = [
    path("books/<int:book_id>/reviews/", ReviewListCreateView.as_view(), name="review-list-create"),
]
