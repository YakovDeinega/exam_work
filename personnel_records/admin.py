from django.contrib import admin

from personnel_records.models import Post, ReasonForAbsence, Employee, Passport, ForeignPassport, MilitaryCard, \
    EmployeeSchedule

# Register your models here.
admin.site.register(Post)
admin.site.register(ReasonForAbsence)
admin.site.register(Employee)
admin.site.register(Passport)
admin.site.register(ForeignPassport)
admin.site.register(MilitaryCard)
admin.site.register(EmployeeSchedule)
