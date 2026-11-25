from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("title/<int:id>/", views.detail, name="detail"),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
]