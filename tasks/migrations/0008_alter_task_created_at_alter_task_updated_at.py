# Generated by Django 4.0.1 on 2022-01-12 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_task_created_at_alter_task_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
