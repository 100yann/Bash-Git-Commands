from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo


# CUSTOM VALIDATOR 
def check_name(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('NAME NEEDS TO START WITH Z')

# FORMS
class FormName(forms.Form):
    name = forms.CharField(validators=[check_name])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    
    # get all data from the forms
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        vmail = cleaned_data.get('verify_email')
        # check if email == verified emails
        if email != vmail:
            raise ValidationError('Make sure emails match!')
        

# NEW USER FORMS
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')