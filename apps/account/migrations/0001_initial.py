# Generated by Django 4.0.1 on 2022-02-02 04:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('organization', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='uploads/profile/', verbose_name='Photo')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email verified')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
