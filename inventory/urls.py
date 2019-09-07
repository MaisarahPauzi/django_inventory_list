from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^laptop$', display_Laptop, name="display_laptop"),
    url(r'^desktop$', display_Desktop, name="display_desktop"),
    url(r'^mobile$', display_Mobile, name="display_mobile")
]