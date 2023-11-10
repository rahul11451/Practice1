from django.urls import path
from .views import upload_pdf, pdf_list

urlpatterns = [
    path('upload/', upload_pdf, name='upload_pdf'),
    path('pdf_list/', pdf_list, name='pdf_list'),
]