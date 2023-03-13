import stripe

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from basket.basket import Basket


@login_required
def BasketView(request):
    basket = Basket(request)
    total = int(basket.get_total_price())*100

    stripe.api_key = 'sk_test_51MlIGjC8D1eyEeaLON8RTdEZ1GOfOzKnSe5Ma3rpW0Mx7Xc07U8o0zHqKRjT5yHhuHNZPn6iimNcYNPUsAO4kI0t00cOCJJy1v'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='czk',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})
