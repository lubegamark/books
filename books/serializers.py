# Serializers define the API representation.
from django.contrib.auth.models import User
from generic_relations.relations import GenericRelatedField
from rest_framework.relations import RelatedField, HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer

from books.models import Book, Author, Publisher, Review, Category, Contributor, Tag, Source, Format, Language


class ReviewGenericRelatedField(RelatedField):
    """
    A custom field to use for the `tagged_object` generic relationship.
    """

    def to_representation(self, value):
        """
        Serialize tagged objects to a simple textual representation.
        """
        if isinstance(value, Book):
            return 'Book: ' + value.__str__()
        raise Exception('Unexpected type of tagged object')


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class BookSerializer(HyperlinkedModelSerializer):
    reviews = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='review-detail'
    )

    tags = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='tag-detail'
    )

    class Meta:
        model = Book
        exclude = ('created_at',)


class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        exclude = ('created_at',)


class PublisherSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        exclude = ('created_at',)


class ContributorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Contributor
        exclude = ('created_at',)


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        exclude = ('created_at',)


class FormatSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Format
        exclude = ('created_at',)


class SourceSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Source
        exclude = ('created_at',)


class LanguageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Language
        exclude = ('created_at',)


class ReviewSerializer(HyperlinkedModelSerializer):
    reviewed_object = GenericRelatedField(
        {
            Book: HyperlinkedRelatedField(
                queryset=Book.objects.all(),
                view_name='book-detail',

            ),
        }, source='content_object', )

    class Meta:
        model = Review
        fields = ('url', 'body', 'rating', 'reviewed_object',)


class TagSerializer(HyperlinkedModelSerializer):
    tagged_object = GenericRelatedField(
        {
            Book: HyperlinkedRelatedField(
                queryset=Book.objects.all(),
                view_name='book-detail',

            ),
        }, source='content_object', )

    class Meta:
        model = Tag
        exclude = ('content_type', 'created_at',)
