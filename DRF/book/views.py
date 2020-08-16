from django.shortcuts import render
from book.models import BookBase
from rest_framework import viewsets
from book.serializers import BookSerializer


class BookView(viewsets.ModelViewSet):
    queryset = BookBase.objects.all()
    serializer_class = BookSerializer


def book_app(request):
    return render(request, 'main_app.html')
