# Generated by Django 4.1.7 on 2023-03-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_alter_barril_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barril',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
