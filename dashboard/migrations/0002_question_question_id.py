# Generated by Django 4.2.7 on 2024-06-28 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
