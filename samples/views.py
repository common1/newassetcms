# from .forms import BookForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import Book
from django.views import generic


class Index(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'samples/index.html'
