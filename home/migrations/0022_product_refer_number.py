# Generated by Django 4.1.1 on 2022-10-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_delete_enquiry_alter_feedback_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Refer_number',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]