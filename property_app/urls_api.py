from django.urls import path

from property_app.views import PropertyApiView, get_property_type

urlpatterns = [
    path("types/property/", get_property_type),
    path("property/", PropertyApiView.as_view()),
    path("property/<int:id>/", PropertyApiView.as_view()),
]
