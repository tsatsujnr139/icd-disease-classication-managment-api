# Generated by Django 2.2.9 on 2020-01-30 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200130_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseaseclassification',
            name='diagnosis_code',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
