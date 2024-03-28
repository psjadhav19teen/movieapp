from django.contrib import admin
from django.urls import path
from moviedemoapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.movie_list, name="movie_list"),
]
