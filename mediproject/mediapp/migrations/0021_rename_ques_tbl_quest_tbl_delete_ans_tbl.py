# Generated by Django 4.1.2 on 2022-11-28 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediapp', '0020_nutrition_tbl'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ques_tbl',
            new_name='quest_tbl',
        ),
        migrations.DeleteModel(
            name='ans_tbl',
        ),
    ]
