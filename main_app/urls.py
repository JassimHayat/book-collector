from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.book_index, name='book-index'),
    path('books/<int:book_id>/', views.book_detail, name='book-detail'),
    path('books/create/', views.BookCreate.as_view(), name='book-create'),
    path('Books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('Books/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    path('accounts/signup/', views.signup, name='signup'),
       
]
