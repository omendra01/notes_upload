# Generated by Django 4.0.4 on 2022-06-08 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0014_alter_download_pdf_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='download_pdf',
            old_name='image',
            new_name='pdf',
        ),
    ]
