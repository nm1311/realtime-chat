"""ChatServerPlayground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from personal.views import (
    home_screen_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home')
]

# Managing the URL's for static files

if settings.DEBUG:
    # If not in producion
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # static () is Helper function to return a URL pattern for serving files in debug mode:
    
    # When we run collectstatic it will copy static files from STATIC_URL and MEDIA_URL to the STATIC_ROOT and MEDIA_ROOT (the places where they will be served from at production whether from the same server or a different server like amazon or nginx)
