# Generated by Django 5.1.3 on 2024-12-03 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]