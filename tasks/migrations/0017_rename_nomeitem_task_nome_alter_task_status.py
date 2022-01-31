# Generated by Django 4.0.1 on 2022-01-31 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_alter_task_orçamento01_alter_task_orçamento02_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='nomeItem',
            new_name='nome',
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('solicitado', 'Solicitado'), ('Comprado', 'Comprado'), ('Aguardando Orçamento', 'Aguardando Orçamento'), ('Recebido', 'Recebido')], max_length=22),
        ),
    ]