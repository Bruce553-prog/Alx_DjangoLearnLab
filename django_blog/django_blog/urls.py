"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views.
For more information, see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin site
    path("admin/", admin.site.urls),

    # Blog app routes (root path)
    path("", include(("blog.urls", "blog"), namespace="blog")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
