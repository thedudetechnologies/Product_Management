from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        print("Inside Register Post")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']     
        print(first_name)
        print(last_name)
        print(email)
        print(password)
        check = User.objects.filter(email=email)
        if check:
            return render(request, 'login.html')
        else:    
            b = User(first_name=first_name, last_name=last_name, email=email,password=password)
            b.save()
        return render(request, 'login.html')

    return render(request, 'register.html')

def login(request):
    
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        m = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = m.id
        checkuser = User.objects.filter(email=email)
        if checkuser:
            pswd = User.objects.filter(email=email,password=password)    
            if pswd:
                request.session['user_id'] = m.id
                request.session['email'] = m.email
                return render(request, 'index.html')
            else:

                return render(request, 'login.html',{'name' : email} )
        else:
            return render(request,'login.html',msg)

   
    return render(request, 'login.html')