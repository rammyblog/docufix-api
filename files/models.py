from django.db import models

class File(models.Model):
    file1 = models.FileField(blank=False, null=False, upload_to="docs")
    file2 = models.FileField(blank=True, null=True, upload_to="docs")

    def __str__(self):
        return str(self.file1.name + self.file2.name)