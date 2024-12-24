from django.db import models

# Create your models here.
class ORDER_STATUS_CHOICES(models.TextChoices):
    Pending = 'Pending', 'Pending'
    Paid = 'Paid', 'Paid'
    Refunded = 'Refunded', 'Refunded'

class Choice_Payment_method(models.TextChoices):
    Credit_Card = 'Credit Card', 'Credit Card'
    PayPal = 'PayPal', 'PayPal'
    Cash = 'Cash', 'Cash'

class Choice_payment_status(models.TextChoices):
    Pending = 'Pending', 'Pending'
    Completed = 'Completed', 'Completed'
    Failed = 'Failed', 'Failed'

class Rating_Choice(models.TextChoices):
    ONE_STAR = '1', '★☆☆☆☆'
    TWO_STAR = '2', '★★☆☆☆'
    THREE_STAR = '3', '★★★☆☆'
    FOUR_STAR = '4', '★★★★☆'
    FIVE_STAR = '5', '★★★★★'

class Author(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    biography = models.TextField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    genre = models.ManyToManyField('Genre', related_name='books')
    isbn = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    description = models.TextField()
    language = models.CharField(max_length=50)
    publication_date = models.DateField()
    image = models.ImageField(upload_to='books/')

    def average_rating(self):
        reviews = self.reviews.all()
        total_rating = sum([review.rating for review in reviews])
        return total_rating / len(reviews) if reviews else 0



    def __str__(self):
        return self.title



class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    account_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    date_of_order = models.DateField()
    shipping_address = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES.choices)
    payment_status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order by {self.customer.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField()
    total_price_per_item = models.DecimalField(max_digits=10, decimal_places=2)


class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='carts')
    items = models.ManyToManyField(Book, through='ShoppingCartItem', related_name='shopping_carts')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.customer.name

class ShoppingCartItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='cart_items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.book.title} in {self.shopping_cart.customer.name}'s Cart"

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=50, choices=Choice_Payment_method.choices)
    payment_date = models.DateField()
    payment_status = models.CharField(max_length=50, choices=Choice_payment_status.choices)
    transaction_id = models.CharField(max_length=50)

    def __str__(self):
        return self.payment_method

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reviews')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=Rating_Choice.choices)
    review_text = models.TextField()
    date_of_review = models.DateField()

    class Meta:
        unique_together = ('customer', 'book')

    def __str__(self):
        return self.customer.name

class Discount(models.Model):
    code = models.CharField(max_length=50, unique=True)
    percentage_discount = models.DecimalField(max_digits=10, decimal_places=2)
    valid_date = models.DateField()
    applicable_books = models.ManyToManyField('Book', related_name='discounts')
    minimum_purchase_requirement = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.code
