from django.urls import path
from . import views 
urlpatterns=[
    path('', views.HomePage, name='homepage'),
    path('addbook/', views.AddBook, name='add_book'),
    path('bookdetails/<int:book_id>/', views.BookDetails, name = 'book_details'),
    path('update/<int:book_id>/', views.UpdateBook, name='update_book'),
    path('delete/<int:book_id>/', views.DeleteBook, name='delete_book'),
]