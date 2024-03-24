from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# class RegistrationForm(forms.ModelForm):
#     """
#     A slighlty modified version of `UserCreationForm`
#     """

#     error_messages = {
#         "password_mismatch": _("The two password fields didn't match."),
#     }
#     password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
#     password2 = forms.CharField(
#         label=_("Password confirmation"),
#         widget=forms.PasswordInput,
#         help_text=_("Enter the same password as above, for verification."),
#     )

#     class Meta:
#         model = User
#         fields = ("first_name", "last_name", "username", "email")

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError(
#                 self.error_messages["password_mismatch"],
#                 code="password_mismatch",
#             )
#         return password2

#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


class RegistrationForm(forms.Form):
    #

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    username = forms.CharField(max_length=100)

    email = forms.EmailField()

    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)