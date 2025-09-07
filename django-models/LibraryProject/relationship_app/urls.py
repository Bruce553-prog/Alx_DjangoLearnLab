from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # import the built-in auth views
from . import views

urlpatterns = [
    # Book and library views
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view

    # Authentication views
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
    path('register/', views.register_view, name='register'), 
]
