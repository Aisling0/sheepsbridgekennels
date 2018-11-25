from django import forms
from captcha.fields import CaptchaField


TYPE_CHOICES = [
    ('Booking Enquiry', 'Booking'),
    ('Grooming Enquiry', 'Grooming'),
    ('General Enquiry', 'Other'),
    ]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    number = forms.CharField(max_length=10)
    mail_type = forms.CharField(label='Enquiry Type', widget=forms.Select(choices=TYPE_CHOICES))
    captcha = CaptchaField()
