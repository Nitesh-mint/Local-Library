from django.shortcuts import render


from .models import Book, BookInstance, Author, Genre

def index(request):
    """Home page view"""
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books 
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The all() is applied default
    num_authors = Author.objects.count()

    # Books that contain particular word
    particular_word_book = Book.objects.filter(title__icontains="Atomic").count()

    context = {
        'num_books':num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors':num_authors,
        'particular_word_book': particular_word_book,
    }
    
    return render(request, 'index.html', context=context)