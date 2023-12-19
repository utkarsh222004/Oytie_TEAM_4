from django.contrib import admin
from service.models import Teacher
from service.models import Student
from service.models import Assignment
from service.models import Batch
from service.models import Solution

class TeacherAdmin(admin.ModelAdmin):
    list_display=('name','username','address','phone','email','password','subject')
class BatchAdmin(admin.ModelAdmin):
    list_display=['batch_name']

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','username','address','phone','email','batch','password')
class AssignmentAdmin(admin.ModelAdmin):
    list_display=('name','batch','teacher_id','questions','deadline')
class SolutionAdmin(admin.ModelAdmin):
    list_display=('stud_id','assign_id','solution','points','comment','submission_date')

admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Batch,BatchAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Assignment,AssignmentAdmin)
admin.site.register(Solution,SolutionAdmin)


# Register your models here.
