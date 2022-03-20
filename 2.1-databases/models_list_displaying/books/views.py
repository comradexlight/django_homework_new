from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def books(request):
    template = 'books/catalog.html'
    all_books_objects = Book.objects.all()
    all_books = [book for book in all_books_objects]
    context = {'books': all_books}
    return render(request, template, context)


def books_date(request, pub_date):
    template = 'books/catalog.html'
    current_date_book = Book.objects.filter(pub_date=pub_date)
    next_date = Book.objects.filter(pub_date__gt=pub_date).dates('pub_date', 'day', order='ASC').first()
    previous_date = Book.objects.filter(pub_date__lt=pub_date).dates('pub_date', 'day', order='ASC').first()

    context = {
        'books': current_date_book,
        'next_date_page': next_date,
        'previous_date_page': previous_date,
    }
    return render(request, template, context)
