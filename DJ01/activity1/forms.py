from django import forms


class RegistrationForm(forms.Form):
    #

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    username = forms.CharField(max_length=100)

    email = forms.EmailField()

    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
