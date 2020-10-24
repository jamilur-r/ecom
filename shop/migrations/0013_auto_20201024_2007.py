# Generated by Django 3.1.2 on 2020-10-24 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_remove_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_ordered',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.product'),
        ),
    ]
