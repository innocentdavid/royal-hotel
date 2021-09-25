from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Driver)
admin.site.register(Customer)
admin.site.register(History)
admin.site.register(Category)
admin.site.register(Room)
admin.site.register(Account)
admin.site.register(HotelConfig)