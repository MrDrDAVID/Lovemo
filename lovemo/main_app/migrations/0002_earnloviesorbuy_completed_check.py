# Generated by Django 3.2.4 on 2021-10-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='earnloviesorbuy',
            name='completed_check',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
