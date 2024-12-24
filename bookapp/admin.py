from django.contrib import admin
from bookapp.models import Book, Author,Publisher,Book,Genre,Customer,Order,OrderItem,ShoppingCart,Payment,Review,Discount,ShoppingCartItem

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'biography', 'nationality')
    list_filter = ('name', 'nationality',)
    search_fields = ('nationality',)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name','email')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'price', 'stock_quantity', 'publication_date',)
    list_filter = ('title', 'isbn')
    search_fields = ('publisher', 'language', 'publication_date')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'account_created')
    search_fields = ('name', 'email')
    list_filter = ('account_created',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_of_order', 'shipping_address', 'order_status')
    search_fields = ('customer__name', 'shipping_address')
    list_filter = ('order_status', 'date_of_order')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'book', 'quantity', 'total_price_per_item')
    search_fields = ('order__customer__name', 'book__title')

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_price')
    search_fields = ('customer__name',)

@admin.register(ShoppingCartItem)
class ShoppingCartItemAdmin(admin.ModelAdmin):
    list_display = ('shopping_cart', 'book', 'quantity', 'price')
    search_fields = ('shopping_cart__customer__name', 'book__title')
    list_filter = ('shopping_cart', 'book')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_method', 'payment_date', 'payment_status', 'transaction_id')
    search_fields = ('order__customer__name', 'transaction_id')
    list_filter = ('payment_method', 'payment_status', 'payment_date')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer', 'book', 'rating', 'date_of_review')
    search_fields = ('customer__name', 'book__title')
    list_filter = ('rating', 'date_of_review')

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'percentage_discount', 'valid_date', 'minimum_purchase_requirement')
    search_fields = ('code',)
    list_filter = ('valid_date',)