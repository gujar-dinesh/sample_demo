from django.conf.urls import url
from . import views as v
app_name= 'product'
urlpatterns=[
url(r'^$', v.showProduct, name='showProduct')
]