from django.contrib import admin
from booking.models import Customer
# Register your models here.

class customeradmin(admin.ModelAdmin):
    list_display = ('name','address','state','city','country')

admin.site.register(Customer,customeradmin)