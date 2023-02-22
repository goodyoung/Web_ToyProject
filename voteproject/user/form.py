from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import UserInfo

class UserInfoForm(forms.ModelForm): # UserCreationForm
    class Meta:
        model = UserInfo
        fields = '__all__'

        
# email = forms.EmailField(label="email")