# Generated by Django 4.0.1 on 2022-01-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='anexo01',
            field=models.FileField(null=True, upload_to='anexos/'),
        ),
        migrations.AddField(
            model_name='task',
            name='anexo02',
            field=models.FileField(null=True, upload_to='anexos/'),
        ),
        migrations.AddField(
            model_name='task',
            name='anexo03',
            field=models.FileField(null=True, upload_to='anexos/'),
        ),
    ]