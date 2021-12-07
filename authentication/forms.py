from django import forms


class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput())


class RemoveBookForm(forms.Form):
  name = forms.CharField()


class AddBookForm(forms.Form):
  name = forms.CharField()