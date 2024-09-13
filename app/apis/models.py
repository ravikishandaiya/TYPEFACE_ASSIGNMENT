from django.db import models

# Create your models here.

class Files(models.Model):
    file_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=50)
    file_path = models.FileField(upload_to='uploads/')
    directory = models.CharField(max_length=1000, default='/')

    def __str__(self):
        return self.file_name