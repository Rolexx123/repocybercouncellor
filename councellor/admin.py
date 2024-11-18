from django.contrib import admin
from .models import Councellor, feedback,rating,complaint

# Register your models here.
admin.site.register(Councellor)
admin.site.register(feedback)
admin.site.register(rating)
admin.site.register(complaint)