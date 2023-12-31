# Generated by Django 5.0 on 2023-12-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_produk', models.CharField(max_length=30)),
                ('nama_produk', models.CharField(max_length=200)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kategori_id', models.CharField(max_length=30)),
                ('status_id', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'produk',
            },
        ),
    ]
