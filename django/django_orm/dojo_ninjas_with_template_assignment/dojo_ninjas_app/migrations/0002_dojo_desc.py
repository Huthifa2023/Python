# Generated by Django 4.2.7 on 2023-11-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
    ]