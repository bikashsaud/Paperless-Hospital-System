from django.contrib import admin
from .models import Patient,D_Medical,D_Lab,Test_result,Medicine
# Register your models here.

admin.site.register(Patient)
admin.site.register(D_Medical)
admin.site.register(D_Lab)
admin.site.register(Medicine)
admin.site.register(Test_result)
