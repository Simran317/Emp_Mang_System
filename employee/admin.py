from django.contrib import admin
from .models import EmployeeDetails,EmployeeEduction,EmployeeExperience,EmpAchievement,Emp_Paper,Emp_Journals
# Register your models here.

admin.site.register(EmployeeDetails)
admin.site.register(EmployeeEduction)
admin.site.register(EmployeeExperience)
admin.site.register(EmpAchievement)
admin.site.register(Emp_Paper)
admin.site.register(Emp_Journals)