from django import forms
from django.forms import fields
from bookclub.models import Discussion


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        # fields have to be passed as a tuple.
        # That means that even if you're passing only one field, the () and the , are necessary
        fields = ("opinion",)
