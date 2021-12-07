
import authentication.glob as glob
from .models import UserInfo, Book
import hashlib

def remove_book(book_name):
  if glob.debug:
    print('removed book: ' + book_name)
    Book.objects.filter(name=book_name).delete()
    return

  if glob.auth:
    print('removed book: ' + book_name)
    Book.objects.filter(name=book_name).delete()


def add_book(book_name):
  if glob.auth:
    print('added book: ' + book_name)
    new_book = Book(name=book_name)
    new_book.save()

def get_books():
  books = Book.objects.all()
  print('retrieved books:', books)
  return books


def admin_login(name, password):
  print('Logged in as admin')
  hashed_password = hashlib.md5(password.encode())
  hashed_password = hashed_password.hexdigest()
  users = UserInfo.objects.filter(username=name, password=hashed_password)
  user = users[0]

  if user != None:
    return True
  else:
    return False



def is_admin():
  return False