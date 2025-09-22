from django.shortcuts import render
from .models import Product
# Create your views here.


def all_products(request):
    """
a view to show all products, including sorting and seearch queries.

    """
    products = product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
