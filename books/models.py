from auditlog.registry import auditlog
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, CharField, DateTimeField, ForeignKey, FloatField, TextField, IntegerField, \
    PositiveIntegerField, ImageField, ManyToManyField, SlugField, URLField
from django.utils.text import slugify


class Author(Model):
    created_at = DateTimeField(auto_now_add=True)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    other_names = CharField(max_length=255)

    def __str__(self):
        return self.first_name+" "+self.last_name


class Contributor(Model):
    created_at = DateTimeField(auto_now_add=True)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    other_names = CharField(max_length=255)
    contribution = CharField(max_length=255)
    content_type = ForeignKey(ContentType)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.first_name+" "+self.last_name


class Publisher(Model):
    created_at = DateTimeField(auto_now_add=True)
    name = CharField(max_length=255)
    other_names = CharField(max_length=255)
    address = CharField(max_length=255)

    def __str__(self):
        return self.name


class Review(Model):
    created_at = DateTimeField(auto_now_add=True)
    author = ForeignKey(User, help_text='Author')
    body = TextField(help_text='Review Text')
    rating = FloatField(help_text='Rating')
    content_type = ForeignKey(ContentType)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.content_object.__str__()+" -"+self.author.__str__()


class Category(Model):
    created_at = DateTimeField(auto_now_add=True)
    category = CharField(max_length=255)
    description = TextField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category


class Tag(Model):
    created_at = DateTimeField(auto_now_add=True)
    content_type = ForeignKey(ContentType)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    tag = CharField(max_length=255)

    def __str__(self):
        return self.tag


class Language(Model):
    created_at = DateTimeField(auto_now_add=True)
    language = CharField(max_length=255)

    def __str__(self):
        return self.language


class Format(Model):
    created_at = DateTimeField(auto_now_add=True)
    format = CharField(max_length=255,)

    def __str__(self):
        return self.format


class Source(Model):
    created_at = DateTimeField(auto_now_add=True)
    source = CharField(max_length=255,)

    def __str__(self):
        return self.source


class Book(Model):
    created_at = DateTimeField(auto_now_add=True)
    title = CharField(max_length=255)
    categories = ManyToManyField(Category, related_name='books')
    publisher = ForeignKey(Publisher, related_name='books')
    published_at = DateTimeField()
    edition = CharField(max_length=255)
    isbn = CharField(max_length=255, verbose_name='ISBN')
    bar_code = CharField(max_length=255,)
    language = ForeignKey(Language, related_name='books')
    audience = CharField(max_length=255,)
    cover_image = ImageField(null=True, blank=True, upload_to='covers')
    parent = ForeignKey('Book',null=True, blank=True,)
    page_count = IntegerField(null=True, blank=True,)
    content_page_count = IntegerField(null=True, blank=True,)
    chapters = IntegerField(null=True, blank=True,)
    tags = GenericRelation(Tag)
    reviews = GenericRelation(Review)
    #MetaData
    availability = ManyToManyField(Source, blank=True, through='BookSource', related_name='available_books')
    formats = ManyToManyField(Format, blank=True, related_name='books')
    views = IntegerField(null=True, blank=True,)
    searches = IntegerField(null=True, blank=True,)
    rating = FloatField(null=True, blank=True,)
    slug = SlugField(unique=True, blank=True,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('book', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class BookSource(Model):
    book = ForeignKey(Book)
    source = ForeignKey(Source)
    link = URLField(null=True, blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.book.__str__(), self.source.__str__())

#Auditing
auditlog.register(Author)
auditlog.register(Contributor)
auditlog.register(Publisher)
auditlog.register(Review)
auditlog.register(Category)
auditlog.register(Tag)
auditlog.register(Language)
auditlog.register(Format)
auditlog.register(Source)
auditlog.register(Book)
auditlog.register(Book.categories.through)
auditlog.register(Book.availability.through)
auditlog.register(Book.formats.through)
