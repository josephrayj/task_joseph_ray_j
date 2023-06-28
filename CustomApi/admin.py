from django.contrib import admin
from .models import Employee,Address,Project,Qualification,WorkExperience

admin.site.register(Employee)
admin.site.register(Address)
admin.site.register(Project)
admin.site.register(Qualification)
admin.site.register(WorkExperience)
