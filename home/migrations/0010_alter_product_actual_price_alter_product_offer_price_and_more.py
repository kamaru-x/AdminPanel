# Generated by Django 4.1.1 on 2022-10-26 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_product_show_enquiry_alter_product_show_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Actual_Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Offer_Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Whatsapp_Number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
