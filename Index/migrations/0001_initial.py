# Generated by Django 3.1 on 2023-06-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(blank=True, max_length=100)),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('business_type', models.CharField(max_length=100)),
                ('kind_of_products', models.CharField(blank=True, max_length=1000)),
                ('company_website', models.CharField(blank=True, max_length=100)),
                ('company_address', models.CharField(blank=True, max_length=500)),
                ('information', models.CharField(blank=True, max_length=1000)),
                ('name_of_person', models.CharField(blank=True, max_length=100)),
                ('contact_email', models.EmailField(max_length=100)),
                ('contact_phone', models.CharField(blank=True, max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
