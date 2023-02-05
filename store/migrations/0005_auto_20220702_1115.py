# Generated by Django 3.2.3 on 2022-07-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210529_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.AddField(
            model_name='category',
            name='addres',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='area',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='closestime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='des',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='opentime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='owner',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50),
        ),
    ]
