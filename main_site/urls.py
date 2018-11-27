from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url(r'^aahc_website/', include('aahc_website.urls')),
    url(r'^main_site/register/',
        RegistrationView.as_view(success_url='/profile/'),
        name='django_registration_register'),
    url(r'^main_site/', include('django_registration.backends.one_step.urls')),
    url(r'^main_site/', include('django.contrib.auth.urls')),
]