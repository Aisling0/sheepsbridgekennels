from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def find(request):

    return render(request, "find.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            mail_type = form.cleaned_data['mail_type']
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            number = form.cleaned_data['number']

            message = "{0} from, {1}\n\n{2}\n\n{3}\n\n{4}".format(mail_type, sender_name, form.cleaned_data['message'],
                                                                  sender_email, number)
            send_mail(mail_type, message, sender_email, ['sheepsbridgekennels@gmail.com'], fail_silently=False)

            if form.is_valid():
                human = True

            return render(request, 'contact_form_sent.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
