# Generated by Django 4.0.1 on 2022-01-31 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0020_rename_nome_do_item_task_nome_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='nome_item',
            new_name='nomeItem',
        ),
    ]
