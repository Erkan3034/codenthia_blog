# Generated by Django 5.2.1 on 2025-06-01 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_bio_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-posta')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
