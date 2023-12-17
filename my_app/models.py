from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Produk(models.Model):
    id_produk = models.CharField(max_length=200)
    nama_produk = models.CharField(max_length=200)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori_id = models.CharField(max_length=200)
    status_id = models.CharField(max_length=200)

    class Meta:
        db_table = 'produk'

class Kategori(models.Model):
    id_kategori  = models.IntegerField()
    nama_kategori = models.CharField(max_length=200)

    class Meta:
        db_table = 'kategori'

class Status(models.Model):
    id_status  = models.IntegerField()
    nama_status = models.CharField(max_length=200)

    class Meta:
        db_table = 'status'