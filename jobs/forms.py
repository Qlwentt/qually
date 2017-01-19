# make sure this is at the top if it isn't already
from django import forms

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