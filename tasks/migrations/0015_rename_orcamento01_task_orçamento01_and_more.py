# Generated by Django 4.0.1 on 2022-01-17 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_rename_orçamento01_task_orcamento01_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='orcamento01',
            new_name='orçamento01',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='orcamento02',
            new_name='orçamento02',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='orcamento03',
            new_name='orçamento03',
        ),
    ]
