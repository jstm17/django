from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect, HttpResponse)
from .models import Product
from .forms import ProductForm, BuyForm

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
              
        if obj.quantity < 1:
                return HttpResponseRedirect("/shop/")
        else:
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
 
    form = BuyForm(request.POST or None)
 
    if request.method =="POST":
        if obj.quantity > int(request.POST['quantity']):
            obj.quantity = obj.quantity - int(request.POST['quantity'])
            obj.save()
        else:
            erreur = "You cannot buy more than " + str(obj.quantity) + ' ' + obj.title
            context = {"erreur": erreur , "form": form, "data" : Product.objects.get(id = id)}
            return render(request, "shop/buy.html", context)

        if obj.quantity < 1:
            return HttpResponseRedirect("/shop/")
        else:
            return HttpResponseRedirect("/shop/"+id)
 
    context = {"form" : form, "data" : Product.objects.get(id = id)}
 
    return render(request, "shop/buy.html", context)