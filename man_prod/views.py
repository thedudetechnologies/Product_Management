from django.shortcuts import render
from .models import Category, Product
from http import *

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
       image = request.POST['image_name']
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



def update(request):
    
    if request.method == 'POST':
            
        
        if 'btn_search' in request.POST:
            global product_ID
            product_ID = request.POST['pid']
            print(product_ID)
            cat = Category.objects.all()
            ckpid = Product.objects.filter(id=product_ID)
            if ckpid:
                prodict = {
                    'product' : ckpid,
                    'cat' : cat
                }
            else:
                prodict = {
                    'msg' : "Item Not Found"
                }
            
            
            return render(request, 'update.html', prodict)

        elif 'btn_update' in request.POST:
            
            product_name = request.POST['product_name']
            #image = request.POST['image_name']
            category = request.POST['category']
            descriptions = request.POST['product_details']
            updated = datetime.datetime.now()
            
            Product.objects.filter(id=product_ID).update(product_name=product_name,category=category,description=descriptions,updated_at=updated)
        
      
        return render(request, 'update.html')
