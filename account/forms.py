from django import forms
from .models import Customer, Address
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm, SetPasswordForm)


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["full_name", "phone", "address_line", "address_line2", "town_city", "postcode"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["full_name"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Celé jméno"}
        )
        self.fields["phone"].widget.attrs.update({"class": "form-control mb-2 account-form", "placeholder": "Telefon"})
        self.fields["town_city"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Město"}
        )
        self.fields["address_line"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Ulice"}
        )
        self.fields["address_line2"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Číslo popisné"}
        )
        self.fields["postcode"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "PSČ"}
        )


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(label='E-mail', widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'login-username'}))
    password = forms.CharField(label='Heslo', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Heslo', 'id': 'login-pwd'}))


class RegistrationForm(forms.ModelForm):
    # name = forms.CharField(label='Uživatelské jméno', min_length=4, max_length=50,)
    email = forms.EmailField(label='E-mail', max_length=100,
                             error_messages={'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Heslo', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Potvrdit heslo', widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('email',)

    # def clean_name(self):
    #     name = self.cleaned_data['name'].lower()
    #     r = Customer.objects.filter(name=name)
    #     if r.count():
    #         raise forms.ValidationError("Username already exists")
    #     return name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs.update(
        #     {'class': 'form-control mb-3', 'placeholder': 'Uživatelské jméno'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Heslo'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Potvrdit heslo'})


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Email (nelze změnit)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email', 'readonly': 'readonly'}))

    name = forms.CharField(
        label='Celé jméno', max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Celé jméno', 'id': 'form-name'}))

    class Meta:
        model = Customer
        fields = ('email', 'name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['name'].required = True


class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(label='E-mail', max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = Customer.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Unfortunatley we can not find that email address')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='Nové heslo', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Nové heslo', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Znovu nové heslo', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Znovu nové heslo', 'id': 'form-new-pass2'}))
