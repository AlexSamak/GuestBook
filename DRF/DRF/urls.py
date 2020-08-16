from django.contrib import admin
from django.urls import path
from book.views import BookView, book_app


from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'api/gbooks', BookView, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_app),
]
urlpatterns += router.urls
