from django.contrib import admin
from .models import Postuser
from .models import PostData
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Postuser)
admin.site.register(PostData)
