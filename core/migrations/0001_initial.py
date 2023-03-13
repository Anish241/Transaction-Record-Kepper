# Generated by Django 4.1.7 on 2023-03-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('amount', models.IntegerField(blank=True)),
            ],
        ),
    ]
