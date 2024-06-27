from django.urls import path

from property_app.views import property_view

urlpatterns = [
    path("", property_view),
]
