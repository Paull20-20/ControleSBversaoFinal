# Generated by Django 4.0.1 on 2022-01-12 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_user_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='quantidade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
