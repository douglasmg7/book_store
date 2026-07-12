from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.db.models import Avg
from .models import Book



def index(request):
    all_books = Book.objects.all().order_by('-title')
    total_number_of_books = all_books.count()
    average_rating = all_books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/index.html', {
        'all_books': all_books, 
        'total_number_of_books': total_number_of_books, 
        'average_rating': average_rating
        })

#  def posts(request):
    #  all_posts_by_date = sorted(posts_data, key=lambda item: item['date'])
    #  return render(request, 'blog/all-posts.html', {"posts": all_posts_by_date})

def book_detail(request, id):
    #  try:
        #  book = Book.objects.get(id=id)
    #  except:
        #  raise Http404
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_outlet/book_detail.html', {'book': book})

def book_detail_by_slug(request, slug):
    #  try:
        #  book = Book.objects.get(id=id)
    #  except:
        #  raise Http404
    book = get_object_or_404(Book, slug=slug)
    #  print(f'Book: {book}')
    return render(request, 'book_outlet/book_detail.html', {'book': book})
