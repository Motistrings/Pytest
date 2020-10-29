from django.contrib import admin
from django.urls import path
import app1.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',app1.views.index)
]

