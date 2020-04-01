from django.shortcuts import render
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

    return render(request, template, context)
