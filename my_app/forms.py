from django import forms  
from my_app.models import Produk  

class ProdukForm(forms.ModelForm):  
    class Meta:  
        model = Produk  
        fields = ['id_produk', 'nama_produk', 'harga', 'kategori_id', 'status_id'] 
        widgets = { 'id_produk': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'nama_produk': forms.TextInput(attrs={ 'class': 'form-control' }),
            'harga': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'kategori_id': forms.TextInput(attrs={ 'class': 'form-control' }),
            'status_id': forms.TextInput(attrs={ 'class': 'form-control' }),
        }