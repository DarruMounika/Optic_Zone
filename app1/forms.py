from django import forms
from .models import login
from django.contrib.auth.models import User



class registerform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','email','password']

    def save(self):
        obj=super().save()
        obj.set_password(self.cleaned_data['password'])
        obj.save()
        return obj
    
class loginform(forms.ModelForm):
    class Meta:
        model=login
        fields='__all__'