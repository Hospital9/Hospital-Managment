from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Patient)
admin.site.register(Appointments)
admin.site.register(BloodTest)