from auditlog.models import LogEntry
from django.contrib import admin

from books.models import Book, Source, Format, Language, Tag, Category, Review, Publisher, Contributor, Author

admin.site.register(Author)
admin.site.register(Contributor)
admin.site.register(Publisher)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Language)
admin.site.register(Format)
admin.site.register(Source)
admin.site.register(Book)


class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp','content_type', 'object_repr', 'action', 'actor', 'remote_addr')
    readonly_fields = ('content_type', 'object_pk', 'object_id', 'object_repr', 'action', 'changes', 'actor',
                       'remote_addr', 'additional_data',)
    pass


admin.site.register(LogEntry, AuditLogAdmin)
