# Generated by Django 5.0.6 on 2024-08-20 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linktee', models.URLField()),
                ('instagram', models.URLField()),
                ('telegram', models.URLField()),
                ('linkedin', models.URLField()),
            ],
        ),
    ]
