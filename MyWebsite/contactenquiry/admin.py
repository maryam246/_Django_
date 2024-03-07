from django.contrib import admin
from contactenquiry.models import contactEnquiry
class ContactAdmin(admin.ModelAdmin): # This allow to show the fields in admin
    list_display = ('name','email','phone','message','websitelink')
                    # modelName # className
admin.site.register(contactEnquiry,ContactAdmin)
# Register your models here.
