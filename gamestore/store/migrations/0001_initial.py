# Generated by Django 4.1.7 on 2023-03-18 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(unique=True)),
                ('author', models.TextField(default='unknown')),
                ('rating', models.IntegerField()),
                ('description', models.TextField()),
                ('genre', models.TextField(default='unknown')),
                ('price', models.FloatField()),
            ],
        ),
    ]
