from django.contrib import admin
from django.urls import path

from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('init/', views.website, name='init')
]
