# ViewSets define the view behavior.
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from books.models import Book, Publisher, Contributor, Author, Review, Category, Tag, Source, Format, Language
from books.serializers import UserSerializer, BookSerializer, ContributorSerializer, \
    PublisherSerializer, AuthorSerializer, ReviewSerializer, CategorySerializer, TagSerializer, SourceSerializer, \
    FormatSerializer, LanguageSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class ContributorViewSet(ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class SourceViewSet(ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class FormatViewSet(ModelViewSet):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer


class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
