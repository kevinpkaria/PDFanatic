# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_pdf, name='upload_pdf'),
    path('chat/<int:pdf_id>/', views.chat, name='chat'),
]
