# Generated by Django 5.0.6 on 2024-08-31 13:51

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password1', models.CharField(max_length=128)),
                ('password2', models.CharField(max_length=128)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('headline', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('experience', models.CharField(max_length=100)),
                ('additional', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password1', models.CharField(max_length=128)),
                ('password2', models.CharField(max_length=128)),
                ('headline', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('skills', models.TextField()),
                ('edu', models.TextField()),
                ('additional', models.TextField()),
                ('cv', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_read', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='Users.alumni')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_notifications', to='Users.student')),
            ],
        ),
    ]
