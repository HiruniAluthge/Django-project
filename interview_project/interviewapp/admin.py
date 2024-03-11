from django.contrib import admin
from .models import School, AssessmentArea, Awards, Student, Subject, Answers, Summary, Class
from import_export.admin import ImportExportModelAdmin

# Registering models
admin.site.register(School,ImportExportModelAdmin)
admin.site.register(AssessmentArea,ImportExportModelAdmin)
admin.site.register(Awards, ImportExportModelAdmin)
admin.site.register(Student,ImportExportModelAdmin)
admin.site.register(Subject,ImportExportModelAdmin)
admin.site.register(Answers,ImportExportModelAdmin)
admin.site.register(Summary,ImportExportModelAdmin)
admin.site.register(Class,ImportExportModelAdmin)
