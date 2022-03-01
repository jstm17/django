from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from .models import Product
from .forms import ProductForm

# PRODUCTS LIST

def list(request):
    context = {"dataset" : Product.objects.all().filter(quantity__gte = 1)}

    return render(request, "shop/index.html", context)

# CREATE PRODUCTS

def create(request):
	context ={}

	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/shop")

	context = {'form' : form}
	return render(request, "shop/create.html", context)

# PRODUCTS DETAILS

def details(request, id):
    context = {"data" : Product.objects.get(id = id)}
         
    return render(request, "shop/details.html", context)

# UPDATE PRODUCTS

def update(request, id):
    obj = get_object_or_404(Product, id = id)
 
    form = ProductForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/shop/"+id)
 
    context = {"form" : form, "data" : Product.objects.get(id = id)}
 
    return render(request, "shop/update.html", context)

# DELETE PRODUCTS

def delete(request, id):
    context = {"data" : Product.objects.get(id = id)}
    obj = get_object_or_404(Product, id = id)
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/shop")
 
    return render(request, "shop/delete.html", context)

# BUY PRODUCTS

def buy(request, id):
    obj = get_object_or_404(Product, id = id)
 
    form = ProductForm(request.POST or None, instance = obj)
    print(obj.quantity - 1)
 
    if request.method =="POST":
        obj.quantity = obj.quantity - 1
        obj.save()
        return HttpResponseRedirect("/shop/"+id)
 
    context = {"form" : form, "data" : Product.objects.get(id = id)}
 
    return render(request, "shop/buy.html", context)

# def buy(request, id):
#     obj = get_object_or_404(Product, id = id)
 
#     form = ProductForm(request.POST or None, instance = obj)
#     print(obj.quantity - 1)
 
#     if request.method =="POST":
#         obj.quantity = obj.quantity - 1
#         obj.save()
#         return HttpResponseRedirect("/shop/"+id)
 
#     context = {"form" : form, "data" : Product.objects.get(id = id)}
 
#     return render(request, "shop/buy.html", context)