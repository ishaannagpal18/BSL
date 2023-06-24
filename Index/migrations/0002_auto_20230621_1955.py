# Generated by Django 3.1 on 2023-06-21 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='company_profile',
            field=models.ImageField(blank=True, upload_to='general_listing'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='image',
            field=models.ImageField(blank=True, upload_to='general_listing'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='small_video',
            field=models.ImageField(blank=True, upload_to='general_listing'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='business_type',
            field=models.CharField(choices=[('yarn', 'yarn'), ('fabric', 'fabric'), ('garment', 'garment'), ('home', 'home'), ('others', 'others')], max_length=15),
        ),
    ]
