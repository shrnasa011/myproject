from django.contrib import admin
from .models import *

class MyUserAdmin(admin.ModelAdmin):
    fields = []

class DoctorAdmin(admin.ModelAdmin):
    fields = []

class HospitalAdmin(admin.ModelAdmin):
    fields = []

class PrescriptionAdmin(admin.ModelAdmin):
    fields = []

class PrescribedMedicineAdmin(admin.ModelAdmin):
    fields = []

class AppointmentAdmin(admin.ModelAdmin):
    fields = []


# Register your models here.
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(PrescribedMedicine, PrescribedMedicineAdmin)
admin.site.register(Appointment, AppointmentAdmin)
