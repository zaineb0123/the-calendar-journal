# Generated by Django 4.0.1 on 2022-03-13 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todoList', models.CharField(max_length=256)),
                ('status', models.BooleanField(default=False)),
                ('dayComplete', models.BooleanField(default=False)),
                ('journal', models.CharField(max_length=2000)),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=120)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_By', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
