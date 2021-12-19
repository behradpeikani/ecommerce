from django import forms
from .models import User, Address

my_default_errors = {
    'required': 'This field is required',
    'invalid': 'The entered phrase is invalid!',
}


class SignInForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'


class SignUpForm(forms.Form):
    first_name = forms.CharField(error_messages=my_default_errors, label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    email = forms.CharField(error_messages=my_default_errors, label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(error_messages=my_default_errors, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(error_messages=my_default_errors, label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError('invalid email, pick another')
        return email

    def clean(self):
        data = self.cleaned_data
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return data


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('phone', 'postcode', 'city', 'address')