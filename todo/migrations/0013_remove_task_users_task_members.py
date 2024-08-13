# Generated by Django 5.0.7 on 2024-08-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_remove_project_created_by_project_users_task_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='users',
        ),
        migrations.AddField(
            model_name='task',
            name='members',
            field=models.CharField(default='Anonymous', max_length=50),
        ),
    ]