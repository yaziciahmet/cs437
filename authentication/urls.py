from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.render_login),
    path('books/', views.render_books)
]
