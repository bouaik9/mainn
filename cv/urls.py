from django.contrib import admin
from django.urls import path, include
from .views import all_resume, update_api, upload_file, remove_person, get_skills, chart, get_one_resume

urlpatterns = [
    path("all/", all_resume, name="all"),

    path("upload/", upload_file, name="upload"),


    path("<id>/<str:variable>/", update_api),

    path("<id>/delete", remove_person),
    path("skills/", get_skills),
    path("", chart),

    path("<id>/", get_one_resume, name="retreive"),

]
