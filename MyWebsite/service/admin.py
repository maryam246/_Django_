from django.contrib import admin
from service.models import Service

# inherit ModelAdmin from admin in class is necessary
class ServiceAdmin(admin.ModelAdmin): # This allow to show the fields in admin
    list_display = ('service_icon','service_title','service_des')
                    # modelName # className
admin.site.register(Service,ServiceAdmin)
# Register your models here.
