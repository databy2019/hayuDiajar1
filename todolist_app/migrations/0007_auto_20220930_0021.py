# Generated by Django 2.2.5 on 2022-09-29 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0006_auto_20220930_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='nilai',
            field=models.IntegerField(default=90),
        ),
    ]
