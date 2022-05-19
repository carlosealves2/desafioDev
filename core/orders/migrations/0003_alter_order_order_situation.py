# Generated by Django 3.2.13 on 2022-05-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_situation',
            field=models.CharField(choices=[('p', 'Pending to send'), ('s', 'Sending'), ('d', 'Delivered')], default='p', max_length=1, verbose_name='Order situation'),
        ),
    ]