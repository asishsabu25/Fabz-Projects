# Generated by Django 4.1.2 on 2022-12-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediapp', '0033_alter_reg_tbl_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrition_tbl',
            name='Time',
            field=models.TextField(default='', max_length=200),
        ),
    ]
