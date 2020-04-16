from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):
    First_Name = forms.CharField(
        label = "First Name",
        widget = forms.TextInput(
            attrs = {
                "id": "FirstName",
                "class": "form-control",
                "placeholder": "First name",
            }
        )
    )
    
    Last_Name = forms.CharField(
        label = "Last Name",
        widget = forms.TextInput(
            attrs = {
                "id": "LastName",
                "class": "form-control",
                "placeholder": "Last name",
            }
        )
    )

    Email = forms.EmailField(
        label = "email",
        widget = forms.EmailInput(
            attrs = {
                "id": "Email",
                "class": "form-control",
                "placeholder": "Email",
            }
        )
    )

    Phone = forms.CharField(
        label = "Phone Number:",
        widget = forms.TextInput(
            attrs = {
                "id": "Phone",
                "class": "form-control",
                "placeholder": "+249123456789",
                "pattern": "^(\+\d{3}?)?\d{9}$",
            }
        )
    )

    Subject = forms.CharField(
        label = "Subject:",
        widget = forms.TextInput(
            attrs = {
                "id": "Subject",
                "class": "form-control",
                "placeholder": "Subject",
            }
        )
    )

    Message = forms.CharField(
        label = "Message:",
        widget = forms.Textarea(
            attrs = {
                "id": "Message",
                "class": "form-control",
                "placeholder": "write your message",
            }
        )
    )
    
    class Meta:
        model = Contact
        fields = "__all__"
