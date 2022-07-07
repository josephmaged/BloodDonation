from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("Home", views.home),
    path("NewDonor", views.newDonor),
    path("About Us", views.aboutUs),
    path("Contact US", views.contactUs)
]
urlpatterns += staticfiles_urlpatterns()
