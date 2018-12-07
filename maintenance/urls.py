from django.urls import path,include
from maintenance import views
urlpatterns = [
    path('503/',views.page_503, name="page_503"),
]