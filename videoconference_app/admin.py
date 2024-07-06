from django.contrib import admin
from .models import userdata
from .models import ContactMessage


# Register your models here.
admin.site.register(userdata)



admin.site.register(ContactMessage)