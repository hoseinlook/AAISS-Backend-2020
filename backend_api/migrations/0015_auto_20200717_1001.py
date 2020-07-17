# Generated by Django 3.0.7 on 2020-07-17 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0014_misc_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='misc',
            name='id',
        ),
        migrations.AddField(
            model_name='misc',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
