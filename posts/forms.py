from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import BlogPost


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    def save(self, commit=True):
        """
        Method that overrides the save() in order to set 'username' equal
        to the 'email' field.
        """
        user = super(RegistrationForm, self).save(commit=False)
        user.username = user.email
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "content"]
