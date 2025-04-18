from django.forms import ModelForm, Form
from django import forms
from bubble.models import Chatroom, User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout, Field

class Room_Form(ModelForm):
    
    class Meta:
        model = Chatroom
        fields = ['name', 'desc', 'image']

   

class User_creation(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class Log_in(forms.Form):

    username = forms.CharField( max_length= 65, required=True)
    password = forms.CharField(max_length = 65, required = True, widget = forms.PasswordInput)


