from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import render
from .forms import LoginForm, AddBookForm, RemoveBookForm
from django.views.generic.base import RedirectView
from .api import  remove_book, add_book, get_books, admin_login,is_admin
import authentication.glob as glob

glob.init_global()


# Create your views here.
def render_login(request):

  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():

      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      
      
      
      success =  admin_login(username, password)

      if success:
        glob.auth = True
        return HttpResponsePermanentRedirect("/books/")

  form = LoginForm()
  return render(request, 'login.html', { 'form': form })




def render_books(request):

  if request.method == 'POST':

    if 'add' in request.POST:
      form = AddBookForm(request.POST)
      if form.is_valid():
        name = form.cleaned_data['name']
        add_book(name)

    elif 'remove' in request.POST:
      form = RemoveBookForm(request.POST)
      if form.is_valid():
        name = form.cleaned_data['name']
        remove_book(name)


  books = get_books()
  add_book_form = AddBookForm()
  remove_book_form = RemoveBookForm()
  return render(request, 'books.html', { 'current_books': books, 'add_book_form': add_book_form, 'remove_book_form': remove_book_form, 'auth': glob.auth })