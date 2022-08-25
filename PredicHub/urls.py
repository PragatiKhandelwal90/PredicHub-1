from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path("admin/", admin.site.urls),

    # Views
    path("/", index, name="index"),

    # Apps
    path("admission/", include("admission.urls")),
    path("job/", include("job.urls")),
]
