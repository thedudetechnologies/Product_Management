from django.shortcuts import render
from .models import Category, Product
from http import *
import datetime
from .forms import ProfileForm

# Create your views here.
def index(request):
    return render(request, 'index.html')



def category(request):
    if request.method == 'POST':
       
        categories = request.POST['categories']
     
        check = Category.objects.filter(name=categories)
        if check:
            pass
        else:    
           Category.objects.create(name=categories)
        
    return render(request, 'category.html')


def add_product(request):

    cat = Category.objects.all()
    catdict = {'cat': cat }
    if request.method == 'POST':
      
       product_name = request.POST['product_name']
       image = request.FILES['file_name']
       category = request.POST['category']
       descriptions = request.POST['product_details']
       check = Product.objects.filter(product_name=product_name)
       if check:
           pass
       else:    
          Product.objects.create(product_name=product_name,image=image,category=category,description=descriptions)
           
    return render(request, 'products.html', catdict )


def crud(request):
    
    product_list = Product.objects.all()
    prodict = {'product' : product_list}
    
    # if request.method == 'POST':
       
    #     categories = request.POST['categories']
     
    #     check = Category.objects.filter(name=categories)
    #     if check:
    #         pass
    #     else:    
    #        Category.objects.create(name=categories)
        
      
    return render(request, 'operations.html', prodict)



def updates(request):
    
    
    if request.method == 'POST':
        print(request.POST)
        global product_ID       
        if 'btn_search' in request.POST:
            
            product_ID = request.POST['pid']
            print("pid",product_ID)
            cat = Category.objects.all()
            ckpid = Product.objects.filter(id=product_ID)
            
            if ckpid:
                print("chpided")
                product_name = Product.objects.values_list('product_name',flat=True).get(id=product_ID)
                product_details = Product.objects.values_list('description',flat=True).get(id=product_ID)
                image = Product.objects.values_list('image',flat=True).get(id=product_ID)
                prodict = {
                    'cat' : cat,
                    'pid' : product_ID,
                    'product_name' : product_name,
                    'description' :product_details,
                    'image' : image,
                }
            else:
                print("else")
                prodict = {
                    'msg' : "Item Not Found"
                }
            
            
            return render(request, 'updates.html', prodict)

        elif 'btn_update' in request.POST:
            product_ID = request.POST['pid_store']
            product_name = request.POST['product_name']
            image = request.FILES['file_name']
            category = request.POST['category']
            descriptions = request.POST['product_details']
            updated = datetime.datetime.now()
            if product_ID:
                Product.objects.filter(id=product_ID).update(product_name=product_name,image=image,category=category,description=descriptions,updated_at=updated)
            else:
                pass
        
      
    return render(request,'updates.html')


def deletes(request):
    product_list = Product.objects.all()
    prodict = {'product' : product_list}
    print("IN delete page")

    if request.method == 'POST':
        pid = request.POST['pid']
        print("delete pid",pid)
        prod = Product.objects.get(id=pid)
        if prod :
            print("item found")
            prod.delete()
            return render(request,'deletes.html', prodict)

        else:
            print("No Item Found")

    return render(request,'deletes.html', prodict)

