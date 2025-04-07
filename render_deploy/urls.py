from django.contrib import admin
from django.urls import path
from example import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", views.users, name="users"),
]
