from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    phone_no=forms.CharField(required=True)

    class Meta:
        model=User
        fields={
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'phone_no',
             }
        field_order=['username','first_name','last_name','email','password1','password2','phone_no']

    def save(self,commit=True):
            user=super(RegistrationForm,self).save(commit=false)
            user.first_name=cleaned_data['first_name']
            user.last_name=cleaned_data['last_name']
            user.email=cleaned_data['email']

            if commit:
                user.save()

            return user



