from django.contrib import admin
from .models import Book, Author, Address

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_filter = ('rating', 'is_bestselling')
    list_display = ('title', 'author')

class AuthorAdmin(admin.ModelAdmin):
    #  list_display = ('first_name', 'last_name')
    pass

class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city')

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)

