# Generated by Django 4.0.4 on 2022-06-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0003_alter_home_notes_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='media')),
            ],
        ),
    ]
