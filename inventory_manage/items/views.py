from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import *
from .forms import *


def main(request):
    items = Item.objects.all()
    context = {
        'items': items
    }

    return render(request, "items/main.html", context)


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item
    }

    return render(request, "items/item_detail.html", context)


def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            return redirect('items:item_detail', item.id)
        return redirect('items:main')
    else:
        form = ItemForm()
        return render(request, "items/item_create.html", {'form': form})


def item_decrease(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.amount -= 1
    item.save()

    return redirect('items:main')


def item_increase(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.amount += 1
    item.save()

    return redirect('items:main')


def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "GET":
        return render(request, "items/item_update.html", {'form': form})
    elif request.method == "POST":
        input_data = request.POST
        input_photo = request.FILES['photo']

        item.name = input_data['name']
        item.photo = input_photo
        item.description = input_data['description']
        item.price = input_data['price']
        item.amount = input_data['amount']
        item.customer = get_object_or_404(Customer, pk=input_data['customer'])
        item.save()

        context = {
            'item': item
        }

        return render(request, "items/item_detail.html", context)


def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "GET":
        context = {
            'item': item
        }

        return redirect('items:item_detail', item.id)
    elif request.method == "POST":
        item.delete()

        return redirect('items:main')


def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }

    return render(request, "items/customer_list.html", context)


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {
        'customer': customer
    }

    return render(request, "items/customer_detail.html", context)


def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('items:customer_detail', customer.id)
        return redirect('items:main')
    else:
        form = CustomerForm()
        return render(request, "items/customer_create.html", {'form': form})


def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "GET":
        form = CustomerForm(instance=customer)

        return render(request, "items/customer_update.html", {'form': form})
    elif request.method == "POST":
        input_data = request.POST

        customer.name = input_data['name']
        customer.tel = input_data['tel']
        customer.address = input_data['address']
        customer.save()

        context = {
            'customer': customer
        }

        return render(request, "items/customer_detail.html", context)


def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "GET":
        context = {
            'customer': customer
        }

        return redirect('items:customer_detail', customer.id)
    elif request.method == "POST":
        customer.delete()

        return redirect('items:main')
