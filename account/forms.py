from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.help_text = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'A user with that email already exists.')
        if 'unn.edu.ng' not in email.split('@')[1]:
            raise forms.ValidationError('Your email has to be a UNN school email.')
        return email


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']
