""" send email import forms """
from django import forms


class ContactForm(forms.Form):
    """ contact form class """
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
