from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Org)
admin.site.register(ChildEduDonor)
admin.site.register(PoorDonor)
admin.site.register(HomeDonor)
admin.site.register(User)
admin.site.register(Receiver)
admin.site.register(Upload)