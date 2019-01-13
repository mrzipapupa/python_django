from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from accounts.models import Accountuser


# class LoginForm(AuthenticationForm):
class LoginForm(forms.ModelForm):
    class Meta:
        model = Accountuser
        fields = ['username', 'password'] # могут быть любые

        widgets = {
            'password': forms.widgets.PasswordInput(
                attrs = {
                    'class': 'field field-password'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DefaultLoginForm(forms.Form):
    username = forms.CharField(
        label='Login',
        max_length=150,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'field field-password'
            }
        )
    )
    password = forms.CharField(
        max_length=72,
        widget=forms.widgets.PasswordInput(
            attrs={
                'class': 'field field-password'
            }
        )
    )

class RegisterForm(UserCreationForm):
    class Meta:
        model = Accountuser
        fields = ('username', 'password1', 'password2', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")


class EditForm(UserChangeForm):
    class Meta:
        model = Accountuser
        fields = {'username', 'age', 'password', 'avatar'}

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")