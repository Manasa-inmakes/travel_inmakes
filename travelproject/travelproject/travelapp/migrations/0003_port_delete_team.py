# Generated by Django 4.2.5 on 2023-11-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='travels')),
            ],
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
