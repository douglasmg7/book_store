from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='book_outlet-index'),
    path('books/<int:id>', views.book_detail, name='book-detail'),
]

