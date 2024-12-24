from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, BookForm, PublisherForm, GenreForm, CustomerForm
from .models import Author, Publisher, Book, Genre, Customer

def home(request):
    return render(request, 'home.html')

def books_list(request):
    books = Book.objects.all()
    return render(request, 'books_list.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bookapp:books_list')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

def edit_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            form.save_m2m()
            return redirect('bookapp:books_list')
        else:
            print(form.errors)
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('bookapp:books_list')
    return render(request, 'delete_book.html', {'book': book})


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('authors_list')
    else:
        form = AuthorForm()
    return render(request, 'create_author.html', context={'form': form})

def edit_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('authors_list')
        else:
            print(form.errors)
    else:
        form = AuthorForm(instance=author)

    return render(request, 'edit_author.html', {'form': form, 'author': author})

def delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('bookapp:authors_list')
    return render(request, 'delete_author.html', context={'author': author})


def publishers_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publishers_list.html', {'publishers': publishers})

def create_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('publishers_list')
    else:
        form = PublisherForm()
    return render(request, 'create_publisher.html', {'form': form})

def edit_publisher(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('bookapp:publishers_list')  # Redirect to the list view
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'edit_publisher.html', {'form': form})

def delete_publisher(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('bookapp:publishers_list')  # Redirect to the list view
    return render(request, 'delete_publisher.html', {'publisher': publisher})

def genres_list(request):
    genres = Genre.objects.all()
    return render(request, 'genres_list.html', {'genres': genres})

def create_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('genres_list')
    else:
        form = GenreForm()
    return render(request, 'create_genre.html', {'form': form})

def edit_genre(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        form = GenreForm(request.POST, request.FILES, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('bookapp:genres_list')
        else:
            print(form.errors)
    else:
        form = GenreForm(instance=genre)
    return render(request, 'edit_genre.html', context={'form': form})

def delete_genre(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        genre.delete()
        return redirect('bookapp:genres_list')
    return render(request, 'delete_genre.html', context={'genre': genre})

def customers_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers_list.html', {'customers': customers})

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customers_list')
    else:
        form = CustomerForm()
    return render(request, 'create_customer.html', context={'form': form})

def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('bookapp:customers_list')
        else:
            print(form.errors)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'edit_customer.html', context={'form': form})

def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('bookapp:customers_list')
    return render(request, 'delete_customer.html', context={'customer': customer})
