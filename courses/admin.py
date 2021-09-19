from django.contrib import admin

# Register your models here.

from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ("c_id","c_name","semestry","year","vacancy","status",)
    
    
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ("courses",)


admin.site.register(Course, CourseAdmin)

