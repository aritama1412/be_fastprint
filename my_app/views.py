from django.shortcuts import render, redirect
from my_app.forms import ProdukForm  
from my_app.models import Produk  
from django.http import JsonResponse
import requests
from django.contrib.auth import authenticate
# from serializers import ProdukSerializer
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def get_data(request):
    api_url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
    username = "tesprogrammer171223C15"
    password = "70d631bc99f745d0935f5ee8a75a2a1e"

    # Set up the request data as form data
    data = {
        'username': username,
        'password': password,
    }

    # Make a GET request to the API
    response = requests.post(api_url, data=data).json()
    # return render(request, 'get_data.html', {'response': response})
    try:
        # Make a POST request to the API
        response = requests.post(api_url, data=data).json()

        # Extract the 'data' key from the API response
        data = response.get('data', [])

        # Save each product to the database
        for produk_data in data:
            product = Produk.objects.create(
                id_produk=produk_data['id_produk'],
                nama_produk=produk_data['nama_produk'],
                harga=produk_data['harga'],
                kategori_id=produk_data['kategori'],
                status_id=produk_data['status'],
            )

        produks = Produk.objects.filter(status_id='bisa dijual')

        return render(request, "index.html",{'produks':produks})  
    except Exception as e:
        # Handle any exceptions that might occur during the request
        return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

def add(request):
    if request.method == "POST":  
        form = ProdukForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except Exception as e:
                pass
    else:  
        form = ProdukForm()  
    return render(request,'add.html', {'form':form})  

def edit(request, id):  
    produk = Produk.objects.get(id=id)  
    return render(request, 'edit.html', {'produk':produk}) 

def update(request, id):  
    produk = Produk.objects.get(id=id)  
    form = ProdukForm(request.POST, instance = produk)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'produk': produk})  
    
def destroy(request, id):  
    produk = Produk.objects.get(id=id)  
    produk.delete()  
    return redirect("/")  

def index(request):
    produks = Produk.objects.filter(status_id='bisa dijual')
    return render(request, "index.html",{'produks':produks})  

def all_data(request):
    produks = Produk.objects.all()  
    return render(request, "all_data.html",{'produks':produks})  
