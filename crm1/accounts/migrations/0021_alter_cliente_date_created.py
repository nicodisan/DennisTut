# Generated by Django 4.1.7 on 2023-03-28 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_cliente_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
