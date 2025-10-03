from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':'pk_test_51SE7XjEiqPK9j07v0cE7uXWP7coky9hDZHhK7jjcDy1W9PDZR9ECdiJkm95VrVIFzldSyrWx4Od39hk4ds6Ldjdu00TKRQki8M',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)