from django.contrib import admin
from .models import maclloc
from .models import courses
from .models import review
from .models import team
# Register your models here.


admin.site.register(maclloc)
admin.site.register(courses)
admin.site.register(review)
admin.site.register(team)
