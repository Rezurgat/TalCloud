from django.urls import path

from .endpoint import views, oauth_view

urlpatterns = [
    path('', oauth_view.google_login),
]
