# Generated by Django 2.0.3 on 2018-11-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAPI', '0002_auto_20181109_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
