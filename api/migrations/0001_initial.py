# Generated by Django 4.2 on 2023-04-14 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.IntegerField()),
                ('available_from', models.CharField(max_length=50)),
                ('available_to', models.CharField(max_length=50)),
            ],
        ),
    ]
