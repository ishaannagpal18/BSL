# Generated by Django 3.1 on 2023-04-15 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0002_remove_register_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='register',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='register',
            name='razorpay_order_id',
        ),
        migrations.RemoveField(
            model_name='register',
            name='razorpay_payment_id',
        ),
        migrations.RemoveField(
            model_name='register',
            name='razorpay_signature',
        ),
    ]
