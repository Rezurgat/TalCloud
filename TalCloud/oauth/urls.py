from django.urls import path

from .endpoint import views, oauth_view

urlpatterns = [
    path('google/', oauth_view.google_auth),
    path('', oauth_view.google_login),
]
