# Generated by Django 4.1.7 on 2023-03-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='mode',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]