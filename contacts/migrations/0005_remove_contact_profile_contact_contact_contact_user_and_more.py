# Generated by Django 4.2.4 on 2023-09-04 02:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0004_alter_contact_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='profile_contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
