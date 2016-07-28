# ViewSets define the view behavior.
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from books.models import Book, Publisher, Contributor, Author, Review, Category, Tag, Source, Format, Language
from books.serializers import UserSerializer, BookSerializer, ContributorSerializer, \
    PublisherSerializer, AuthorSerializer, ReviewSerializer, CategorySerializer, TagSerializer, SourceSerializer, \
    FormatSerializer, LanguageSerializer


class UserViewSet(ModelViewSet):
    """
    This endpoint presents the users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(ModelViewSet):
    """
    This Endpoint presents the books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PublisherViewSet(ModelViewSet):
    """
    This Endpoint presents the publishers
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class ContributorViewSet(ModelViewSet):
    """
    This Endpoint presents the contributors
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class AuthorViewSet(ModelViewSet):
    """
    This Endpoint presents the authors
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ReviewViewSet(ModelViewSet):
    """
    This Endpoint presents the Reviews
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CategoryViewSet(ModelViewSet):
    """
    This Endpoint presents the categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(ModelViewSet):
    """
    This Endpoint presents the tags
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class SourceViewSet(ModelViewSet):
    """
    This Endpoint presents the sources
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class FormatViewSet(ModelViewSet):
    """
    This Endpoint presents the formats
    """
    queryset = Format.objects.all()
    serializer_class = FormatSerializer


class LanguageViewSet(ModelViewSet):
    """
    This Endpoint presents the languages
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
