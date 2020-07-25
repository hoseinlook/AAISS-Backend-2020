# Generated by Django 3.0.7 on 2020-07-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0027_auto_20200725_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='level',
            field=models.CharField(blank=True, choices=[('NOT_ASSIGNED', 'NOT_ASSIGNED'), ('Elementary', 'Elementary'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='NOT_ASSIGNED', max_length=15),
        ),
    ]
