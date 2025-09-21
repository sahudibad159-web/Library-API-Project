from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# import yung hiwa-hiwalay na api files
from .api.user_api import user_urlpatterns
from .api.book_api import book_urlpatterns
from .api.review_api import review_urlpatterns

urlpatterns = (
    user_urlpatterns
    + book_urlpatterns
    + review_urlpatterns
    + [
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    ]
)
