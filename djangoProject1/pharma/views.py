from django.shortcuts import render,get_list_or_404,redirect
from .models import MedicineDetails,OrderItem,Order
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.http import HttpResponse
from .forms import Orderform, CreateUserForm

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def index(request):
    context = {'medicine': MedicineDetails.objects.all()}

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def shop(request):
    medicine = MedicineDetails.objects.all()
    return render(request, 'shop.html', {'medicine': medicine})


def shop_single(request):
    medicine = MedicineDetails.objects.all()
    return render(request, 'shop-single.html', {'medicine': medicine})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items}
    return render(request, 'cart.html', context)

@login_required(login_url='login')
def checkout(request):
    return render(request, 'checkout.html')


class homeview(ListView):
    model = MedicineDetails
    template_name = "index.html"

class itemdetailview(DetailView):
    model = MedicineDetails
    template_name = "shop-single.html"
class OrderSummary(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, complete=False)
        except ObjectDoesNotExist:
            return redirect("/")


        return render(self.request,'cart.html')



def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = MedicineDetails.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

