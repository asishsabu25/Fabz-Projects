# Generated by Django 4.1.2 on 2022-11-18 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediapp', '0002_alter_reg_tbl_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ques_tbl',
            name='Replay',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ques_tbl',
            name='Status',
            field=models.CharField(default='', max_length=50),
        ),
    ]
