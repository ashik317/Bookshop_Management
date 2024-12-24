import random
from django.core.management.base import BaseCommand
from bookapp.models import Author, Publisher, Book, Genre, Customer

class Command(BaseCommand):
    help = "Populate the database with sample data"

    def handle(self, *args, **kwargs):
        # Create Genres
        genres = [
            Genre.objects.get_or_create(name="Fiction", description="Fictional books")[0],
            Genre.objects.get_or_create(name="Science", description="Science books")[0],
            Genre.objects.get_or_create(name="History", description="History books")[0],
            Genre.objects.get_or_create(name="Adventure", description="Adventure books")[0],
        ]

        # Create Authors
        authors = []
        for i in range(5):
            author = Author.objects.get_or_create(
                name=f"Author {i+1}",
                date_of_birth="1980-01-01",
                biography=f"Biography of Author {i+1}",
                nationality="American",
            )[0]
            authors.append(author)

        # Create Publishers
        publishers = []
        for i in range(3):
            publisher = Publisher.objects.get_or_create(
                name=f"Publisher {i+1}",
                address=f"123 Publisher St {i+1}",
                phone=f"555-1234-{i+1}",
                email=f"publisher{i+1}@example.com",
            )[0]
            publishers.append(publisher)

        # Create Books
        for i in range(15):
            book = Book.objects.get_or_create(
                title=f"Book {i+1}",
                author=random.choice(authors),
                publisher=random.choice(publishers),
                price=random.uniform(10.0, 100.0),
                stock_quantity=random.randint(1, 20),
                isbn=f"1234567890{i}",
                description=f"This is the description for Book {i+1}.",
                language="English",
                publication_date="2023-01-01",
            )[0]
            book.genre.set(random.sample(genres, random.randint(1, len(genres))))

        # Create Customers
        for i in range(5):
            Customer.objects.get_or_create(
                name=f"Customer {i+1}",
                email=f"customer{i+1}@example.com",
                phone=f"555-5678-{i+1}",
                address=f"456 Customer St {i+1}",
                date_of_birth="1995-01-01",
            )

        self.stdout.write(self.style.SUCCESS("Sample data populated successfully."))
