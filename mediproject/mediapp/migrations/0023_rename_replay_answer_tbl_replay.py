# Generated by Django 4.1.2 on 2022-11-30 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediapp', '0022_answer_tbl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer_tbl',
            old_name='Replay',
            new_name='replay',
        ),
    ]
