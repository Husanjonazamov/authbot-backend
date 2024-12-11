# Generated by Django 5.1.3 on 2024-12-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('random_code', models.IntegerField(max_length=6)),
                ('is_verified', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]