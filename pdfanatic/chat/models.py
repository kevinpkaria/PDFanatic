from django.db import models

class PDFFile(models.Model):
    file = models.FileField(upload_to='pdf_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ChatHistory(models.Model):
    question = models.TextField()
    answer = models.TextField()
    pdf_file = models.ForeignKey(PDFFile, on_delete=models.CASCADE)
