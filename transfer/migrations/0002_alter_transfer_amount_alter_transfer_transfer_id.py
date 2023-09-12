# Generated by Django 4.2.4 on 2023-08-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='transfer_id',
            field=models.CharField(max_length=12),
        ),
    ]