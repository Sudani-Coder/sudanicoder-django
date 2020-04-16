from django.shortcuts import render, redirect
from django.contrib import messages
from contact.models import Contact
from contact.forms import ContactForm

# Create your views here.


def index(request):
    template = "contact/index.html"
    form = ContactForm()
    context = {"form": form}

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Your message was sent successfully, We will respond to you as soon as possible Thank you for contacting us!'
            )
            return redirect('contact:contact')

    return render(request, template, context)

def contact(request):
    return render(request, "contact/contact.html")
