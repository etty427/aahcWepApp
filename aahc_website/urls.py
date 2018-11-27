
from django.contrib import admin
from django.conf.urls import url

from main_site import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', views.index, name='index'),
]
