# Generated by Django 4.0.4 on 2022-06-15 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0017_rename_emial_contact_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='download_pdf',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]