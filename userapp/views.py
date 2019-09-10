from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html') 

def register(request):
    return render(request,'register.html') 

def contact(request):
    return render(request,'contact.html') 

def shop(request):
    return render(request,'shop.html') 

def single(request):
    return render(request,'single.html')
    
def about(request):
    return render(request,'about.html')  

def coming(request):
    return render(request,'coming.html')        

def logout(request):
    auth.logout(request)
    return redirect('/')

def registerapi(request):

    if request.method == "POST":
        username = request.POST['text1']
        email = request.POST['text2']
        password = request.POST['password']
        print(username,email,password)

        if User.objects.filter(username=username).exists():
            print('username taken ')
            messages.info(request,'username already taken')
            return redirect('/register')

        elif User.objects.filter(email=email).exists():
            print('email taken')
            messages.info(request,'email already taken')
            return redirect('/register')

        else:
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
            print('user created')
            messages.success(request,'user created')
            return redirect('/register')

    else:
        return render(request,'register.html')


def loginapi(request):

    if request.method == "POST":
        username = request.POST['text1']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        hi = User.objects.get(username=username)
        print("manjesh",user,">",hi.id)
        if user is not None:
            auth.login(request,user)
            response = HttpResponse("Cookie Set")  
            response.set_cookie('java-tutorial', 'javatpoint.com')  
            messages.success(request,'login successfull')
            return redirect('/about')

        else:
            messages.info(request,'Invalid credentials')
            return redirect('/login')

    else:
        return render(request,'login.html')        