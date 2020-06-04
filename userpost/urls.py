from django.conf.urls import url
from . import views as v
app_name= 'post'
urlpatterns=[
url(r'^$', v.post, name='post')
]