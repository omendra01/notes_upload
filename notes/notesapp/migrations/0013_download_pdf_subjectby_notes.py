# Generated by Django 4.0.4 on 2022-06-08 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0012_download_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='download_pdf',
            name='subjectby_notes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='notesapp.subjectby_notes'),
            preserve_default=False,
        ),
    ]