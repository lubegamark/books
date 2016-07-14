from django.views.generic import ListView

from books.models import Book


class IndexView(ListView):
    model = Book
    template_name = 'index.html'