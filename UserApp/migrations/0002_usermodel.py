# Generated by Django 5.1.6 on 2025-02-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('password_hash', models.CharField(max_length=255)),
                ('secret_key', models.TextField()),
                ('encryption_key', models.TextField()),
                ('block_hash', models.CharField(max_length=255)),
                ('signature', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'UserModel',
            },
        ),
    ]
