from django.contrib import admin

from .models import Book, Author, BookInstance, Language, Genre

class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    fields = ['title','summary',('isbn','genre','language')]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','date_of_birth', 'date_of_date',)
    fields = ['first_name', 'last_name', ('date_of_birth','date_of_date')]

    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)    # Using the old register method

"""Adding a class for the functionality to edit BookInstance model in the BookAmin page"""
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0 # Don't show already available copies

"""Using the @register decorator for registering the app like the method"""
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','due_back','id')
    list_filter = ('status', 'due_back') # For the side bar to show on admin panel

    fieldsets = (
        (None, {
            'fields' :('book', 'imprint','id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )

admin.site.register(Language)
admin.site.register(Genre)