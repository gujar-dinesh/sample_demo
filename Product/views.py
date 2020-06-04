from django.shortcuts import render
from .models import products as p
# Create your views here.
def showProduct(request):
	products=p.objects.all()
	return render(request,"product/products.html",{'product':products})