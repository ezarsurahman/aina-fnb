# Generated by Django 5.1.1 on 2024-09-15 08:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_foodentry_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodentry',
            name='img',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foodentry',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
