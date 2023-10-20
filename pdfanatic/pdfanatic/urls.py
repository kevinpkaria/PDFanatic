"""
URL configuration for pdfanatic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# your_django_project/urls.py

from django.contrib import admin
from django.urls import include, path
from chat.views import upload_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_pdf, name='upload_pdf'),  # Add this line to map the root URL to the "Upload PDF" view
    path('chat/', include('chat.urls')),
]



