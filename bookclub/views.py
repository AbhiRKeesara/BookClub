from datetime import date

from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from bookclub.forms import DiscussionForm
from bookclub.models import Book

# Create your views here.


def all_books(request):
    # retrieve all records of the Book model
    books = Book.objects.all()
    upcoming_books = Book.objects.filter(read_by__gte=date.today()).order_by("read_by")[
        :3
    ]
    previous_books = Book.objects.filter(read_by__lt=date.today()).order_by("-read_by")[
        :3
    ]
    return render(
        request,
        "bookclub/all_books.html",
        {
            "books": books,
            "upcoming_books": upcoming_books,
            "previous_books": previous_books,
        },
    )


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    discussion_form = DiscussionForm()
    discussion_open = False
    if book.read_by <= date.today():
        discussion_open = True
    if request.method == "POST":
        form = DiscussionForm(request.POST)

        if not request.user.is_anonymous:

            if form.is_valid():
                opinion = form.save(commit=False)
                opinion.author = request.user
                opinion.book = book
                opinion.save()

                return redirect("book_detail", pk=book.pk)
        else:
            return HttpResponseForbidden("Forbidden")

    return render(
        request,
        "bookclub/book_detail.html",
        {
            "book": book,
            "discussion_open": discussion_open,
            "discussion_form": discussion_form,
        },
    )
