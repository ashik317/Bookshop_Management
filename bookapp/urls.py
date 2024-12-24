from django.urls import path
from . import views

app_name = 'bookapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', views.authors_list, name='authors_list'),
    path('publishers/', views.publishers_list, name='publishers_list'),
    path('books/', views.books_list, name='books_list'),
    path('genres/', views.genres_list, name='genres_list'),
    path('customers/', views.customers_list, name='customers_list'),
    path('create_book/', views.create_book, name='create_book'),
    path('create_author/', views.create_author, name='create_author'),
    path('<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('authors/<int:author_id>/edit/', views.edit_author, name='edit_author'),
    path('authors/<int:author_id>/delete/', views.delete_author, name='delete_author'),
    path('publishers/create/', views.create_publisher, name='create_publisher'),
    path('publisher/edit/<int:pk>/', views.edit_publisher, name='edit_publisher'),
    path('publishers/<int:pk>/delete/', views.delete_publisher, name='delete_publisher'),
    path('create_genre/', views.create_genre, name='create_genre'),
    path('genre/edit/<int:pk>/', views.edit_genre, name='edit_genre'),
    path('genre/delete/<int:pk>/', views.delete_genre, name='delete_genre'),
    path('customers/create/', views.create_customer, name='create_customer'),
    path('customers/edit/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('create_customer/delete/<int:pk>/', views.delete_customer, name='delete_customer'),
]
