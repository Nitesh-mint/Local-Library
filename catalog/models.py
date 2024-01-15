from django.db import models
from django.urls import reverse
import uuid

class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        unique = True,
        help_text = "Enter a book genre (e.g. Science Fiction, Romance etc)"
    )


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])

class Language(models.Model):
    name = models.CharField(
        max_length=100,
        unique =True,
        help_text = "Enter the book's natural language")
    
    def get_absolute_url(self):
        return reverse('language-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length= 200)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT)
    summary = models.TextField(
        max_length=1000,
        help_text = "Enter a brief description of book"
    )
    isbn = models.CharField(
        max_length = 16,
        help_text = "Enter the isbn number of the book",
        )
    genre = models.ManyToManyField(
        Genre, help_text="Select a genre for this book")
    
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        """Create a string for genre. This is done because it genre is ManyToManyField."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'
    
class BookInstance(models.Model):
    """ Model representing a specific copy of book (i.e that can be borrowed from 
    the library)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text= "Unique ID for this particular book across the whole library")
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices = LOAN_STATUS,
        blank = True,
        default = 'm',
        help_text = "Book availability",
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'
    



class Author(models.Model):
    first_name = models.CharField(
        max_length = 100,
        help_text = "Enter the firstname of the author"
    )
    last_name = models.CharField(
        max_length = 100,
        help_text = "Enter the lastname of the author"
    )
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_date = models.DateField('Died', null=True, blank=True) # 'Died' here will be shown in admin panel instead of fieldname

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

