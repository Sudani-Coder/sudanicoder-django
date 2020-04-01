from django.contrib import admin
from contact.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ("First_Name", "Last_Name", "Email", "Phone", "Subject", "created")
    list_filter = ["created"]

admin.site.register(Contact, ContactAdmin)
