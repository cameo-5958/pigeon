# Generated by Django 5.2.1 on 2025-05-25 20:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='uploads/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
