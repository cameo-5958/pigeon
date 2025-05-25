from django.urls import path
from . import views

app_name = "files"

urlpatterns = [
        path("download/<str:filename>/", views.download_file, name='download'),
        path("upload/success/", views.upload_success, name="upload_success"),
        path("upload/", views.upload_file, name='upload'),
        ]
