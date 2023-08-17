from django.shortcuts import render, redirect
from .models import Dish, Order
from .forms import DishForm, OrderForm
from django.core.paginator import Paginator


def home(request):
    return render(request, 'zomato_app/home.html')


def dish_list(request):
    dish_list = Dish.objects.all()
    # Change 5 to the desired number of items per page
    paginator = Paginator(dish_list, 5)
    page_number = request.GET.get('page')
    dishes = paginator.get_page(page_number)
    return render(request, 'zomato_app/dish_list.html', {'dishes': dishes})


def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm()
    return render(request, 'zomato_app/add_dish.html', {'form': form})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'zomato_app/order_list.html', {'orders': orders})


def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'zomato_app/place_order.html', {'form': form})
