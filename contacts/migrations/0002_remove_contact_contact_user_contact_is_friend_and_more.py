# Generated by Django 4.2.4 on 2023-09-03 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0012_alter_userprofile_profile_picture'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_user',
        ),
        migrations.AddField(
            model_name='contact',
            name='is_friend',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='profile_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
