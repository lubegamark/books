# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers

from books.viewsets import UserViewSet, BookViewSet, PublisherViewSet, AuthorViewSet, ContributorViewSet, \
    CategoryViewSet, ReviewViewSet, TagViewSet, SourceViewSet, FormatViewSet, LanguageViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'contributors', ContributorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'tags', TagViewSet)
router.register(r'sources', SourceViewSet)
router.register(r'formats', FormatViewSet)
router.register(r'languages', LanguageViewSet)

