from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, BookListCreateView, ReviewListCreateView, BookDetailView

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="login"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:book_id>/reviews/", ReviewListCreateView.as_view(), name="review-list-create"),
    path("books/<int:book_id>/", BookDetailView.as_view(), name="book-detail"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
]
