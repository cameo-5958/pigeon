import uuid
import os
import hashlib
from django.db import models

def hashed_upload_path(instance, filename):
    hash_name = f"{uuid.uuid4()}"
    return os.path.join(hash_name)

class UploadedFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to=hashed_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    file_size = models.PositiveIntegerField(null=True, blank=True)  # size in bytes
    file_hash = models.CharField(max_length=64, null=True, blank=True)  # sha256 hex digest
    file_name = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        is_new = self.pk and self.file

        original_filename = self.file.name.split("/")[-1] if is_new else None

        super().save(*args, **kwargs)  # Save file first, so file.path exists
        
        updated_fields=['file_size','file_hash',]

        if self.file and not self.file_name and original_filename:
            self.file_name = original_filename
            updated_fields.append('file_name')

        # Compute file size
        if self.file and not self.file_size:
            self.file_size = self.file.size  # in bytes

        # Compute SHA256 hash of file content
        if self.file and not self.file_hash:
            sha256 = hashlib.sha256()
            with open(self.file.path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    sha256.update(chunk)
            self.file_hash = sha256.hexdigest()

        # Save again with updated fields, but avoid recursion by checking update flag
        super().save(update_fields=updated_fields)

    def __str__(self):
        return self.file.name

