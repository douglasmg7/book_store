from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_filter = ('rating', 'is_bestselling')
    list_display = ('title', 'author')

# Register your models here.
admin.site.register(Book, BookAdmin)

