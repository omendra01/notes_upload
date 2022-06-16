# Generated by Django 4.0.4 on 2022-06-07 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0007_notes_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes_price',
            name='biology_actual_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes_price',
            name='biology_discount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes_price',
            name='chemistry_actual_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes_price',
            name='chemistry_dicount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes_price',
            name='geography_actual_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes_price',
            name='geography_discount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes_price',
            name='history_actual_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes_price',
            name='history_discount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes_price',
            name='physics_actual_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes_price',
            name='physics_discount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes_price',
            name='polity_actual_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes_price',
            name='polity_discount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]