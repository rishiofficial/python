# Generated by Django 5.0.4 on 2024-04-09 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='country',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
    ]