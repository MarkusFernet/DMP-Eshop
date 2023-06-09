from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, UserEditForm, UserAddressForm
from .token import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .models import Customer, Address
from django.contrib.auth import login, logout
from store.models import Product
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from orders.models import Order
from orders.views import user_orders


@login_required
def dashboard(request):
    return render(request, 'account/dashboard/dashboard.html')


@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request, 'account/dashboard/edit_details.html', {'user_form': user_form})


@login_required
def delete_user(request):
    user = Customer.objects.get(email=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('account:delete_confirmation')


def account_register(request):

    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            html_message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message=None, html_message=html_message)
            return render(request, 'account/registration/register_email_confirm.html', {'form': registerForm})

    else:
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form': registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Customer.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('store:store_home')
    else:
        return render(request, 'account/registration/activation_invalid.html')


# Addresses

@login_required
def view_address(request):
    addresses = Address.objects.filter(customer=request.user)
    return render(request, "account/dashboard/addresses.html", {"addresses": addresses})


@login_required
def add_address(request):
    global previous_url_aa
    if request.method == "POST":
        address_form = UserAddressForm(data=request.POST)
        if address_form.is_valid():
            address_form = address_form.save(commit=False)
            address_form.customer = request.user
            address_form.save()
            if "delivery_address" in previous_url_aa:
                return redirect("checkout:delivery_address")
            return HttpResponseRedirect(reverse("account:addresses"))
    else:
        address_form = UserAddressForm()
        previous_url_aa = request.META.get("HTTP_REFERER")

    return render(request, "account/dashboard/edit_addresses.html", {"form": address_form})


@login_required
def edit_address(request, id):
    global previous_url_ea
    if request.method == "POST":
        address = Address.objects.get(pk=id, customer=request.user)
        address_form = UserAddressForm(instance=address, data=request.POST)
        if address_form.is_valid():
            address_form.save()
            if "delivery_address" in previous_url_ea:
                return redirect("checkout:delivery_address")
            return HttpResponseRedirect(reverse("account:addresses"))
    else:
        address = Address.objects.get(pk=id, customer=request.user)
        address_form = UserAddressForm(instance=address)
        previous_url_ea = request.META.get("HTTP_REFERER")

    return render(request, "account/dashboard/edit_addresses.html", {"form": address_form})


@login_required
def delete_address(request, id):
    address = Address.objects.filter(pk=id, customer=request.user).delete()
    if 'address' in request.session:
        del request.session['address']
    return redirect("account:addresses")


@login_required
def set_default(request, id):
    Address.objects.filter(customer=request.user, default=True).update(default=False)
    Address.objects.filter(pk=id, customer=request.user).update(default=True)

    previous_url_sd = request.META.get("HTTP_REFERER")

    if "delivery_address" in previous_url_sd:
        return redirect("checkout:delivery_address")

    return redirect("account:addresses")


@login_required
def wishlist(request):
    products = Product.objects.filter(users_wishlist=request.user)
    return render(request, "account/dashboard/user_wishlist.html", {"wishlist": products})


@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    is_in_wishlist = product.users_wishlist.filter(id=request.user.id).exists()
    if is_in_wishlist:
        product.users_wishlist.remove(request.user)
    else:
        product.users_wishlist.add(request.user)

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return render(request, "account/dashboard/user_orders.html", {"orders": orders})
