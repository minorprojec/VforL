from django.shortcuts import render , HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
from .models import Shop
from .forms import *
from django.contrib.auth.models import User, auth

# Create your views here.

def home(request):
    return render(request,'index.html')

def add(request):
    return render(request,'add.html')
    

def thirdpage(request):
    if request.method=='POST':
        shop_owner_name = request.POST["shop_owner_name"]
        shop_name = request.POST["shop_name"]
        address = request.POST["address"]
        contact_no = request.POST["contact_no"]
        home_delievery = request.POST["home_delievery"]
        description = request.POST["description"]

        user = User.objects.create_user(shop_owner_name=shop_owner_name, shop_name=shop_name, address=address, contact_no=contact_no, home_delievery=home_delievery, description=description)
        user.save();
        print('Shop details are added')
        return redirect('thirdpage')

    else:
        return render(request,'add.html')
    
    

def secondpage(request):
    return render(request,'business.html')

def grocerypage(request):
    return render(request,'grocery.html')

def gurudevpage(request):
    return render(request,'gurudev.html')

def gauravpage(request):
    return render(request,'gaurav.html')

def fruitshop(request):
    return render(request,'fruitshop.html')

def headerpage(request):
    return render(request,'header.html')

def footerpage(request):
    return render(request,'footer.html')


    

    """ 
    print("Shop details is add.")
    shop_owner_name = request.POST["shop_owner_name"]
    shop_name = request.POST["shop_name"]
    address = request.POST["address"]
    contact_no = request.POST["contact_no"]
    home_delievery = request.POST["home_delievery"]
    description = request.POST["description"]

    Shop = Shop(shop_owner_name=shop_owner_name,shop_name=shop_name,address=address,contact_no=contact_no,home_delievery=home_delievery,description=description)
    
    Shop.save()
    """
   
def localshop(request):
    if request.method == 'POST':

        form = Shop_details(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/localshop/')
    
    else:
        form = Shop_details()
    return render(request, 'shop.html', {'form':form})
    
