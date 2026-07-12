from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Book



def index(request):
    all_books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {'all_books': all_books})

#  def posts(request):
    #  all_posts_by_date = sorted(posts_data, key=lambda item: item['date'])
    #  return render(request, 'blog/all-posts.html', {"posts": all_posts_by_date})

def book_detail(request, id):
    #  try:
        #  book = Book.objects.get(id=id)
    #  except:
        #  raise Http404
    book = get_object_or_404(Book, id=id)
    print(f'Book: {book}')
    return render(request, 'book_outlet/book_detail.html', {'book': book})
