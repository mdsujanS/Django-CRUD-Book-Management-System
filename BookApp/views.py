from django.shortcuts import render, redirect
from .models import Book 
from .forms import BookForm 

# Create your views here.
def HomePage(request):
    books = Book.objects.all()
    context={
        'books' : books
    }
    return render(request, 'book_list.html', context)

def AddBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForm() 
    return render(request, 'add_book.html', {'form' : form}) 

def BookDetails(request, book_id):
    book = Book.objects.get(id=book_id)
    
    return render(request, 'details.html', {'book' : book})

def UpdateBook(request, book_id):
    book = Book.objects.get(id = book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForm(instance=book)
    return render(request, 'add_book.html', {'form' : form})

def DeleteBook(request, book_id):
    book = Book.objects.get(id= book_id)
    if book:
        book.delete()
    return redirect('homepage')  

