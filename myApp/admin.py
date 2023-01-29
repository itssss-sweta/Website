from django.contrib import admin
from myApp.models import AccessRecord, Webpage,Contact,Topics
# Register your models here.
admin.site.register(Contact)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(Topics)

