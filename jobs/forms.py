# make sure this is at the top if it isn't already
from django import forms

from django.contrib.auth.models import User
from models import Profile
from django.contrib.auth.forms import UserCreationForm

# our new form
class SeeJobsForm(forms.Form):
    job_title = forms.CharField(required=True)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    yrs_exp = forms.IntegerField(required=True)
    resume = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('job_title', 'yrs_exp', 'resume', 'city', 'state')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")