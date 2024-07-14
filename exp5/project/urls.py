from django.contrib import admin
from django.urls import path

from myapp.views import course_search, reg, cts_view  # Import the new view

urlpatterns = [
    path('secretadmin/', admin.site.urls),
    path('cts/<int:s>/<int:n>', cts_view),  # Include the new view function
    path('reg/', reg),
    path('course_search/', course_search),
]
