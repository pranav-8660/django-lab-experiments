from django.contrib import admin
from django.urls import path

from myapp.views import course_search, reg, cts_view  # Import the new view

urlpatterns = [
    path('secretadmin/', admin.site.urls),
]
