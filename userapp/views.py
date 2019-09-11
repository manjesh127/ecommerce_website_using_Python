from django.shortcuts import render , redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import jwt
# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html') 

def register(request):
    return render(request,'register.html') 

def contact(request):
    manjesh = request.COOKIES
    
    if not manjesh:
        return redirect('/')
    elif manjesh=="":
        return redirect('/')
    elif 'token' in manjesh:
        return render(request,'contact.html') 
    else:
        return redirect('/')
     

def shop(request):
    manjesh = request.COOKIES
    
    if not manjesh:
        return redirect('/')
    elif manjesh=="":
        return redirect('/')
    elif 'token' in manjesh:
        
        return render(request,'shop.html') 
    else:
        return redirect('/') 
    

def single(request):
    manjesh = request.COOKIES
    
    if not manjesh:
        return redirect('/')
    elif manjesh=="":
        return redirect('/')
    elif 'token' in manjesh:
        
        return render(request,'single.html')
    else:
        return redirect('/') 
    
    
def about(request):
    manjesh = request.COOKIES
    
    if not manjesh:
        return redirect('/')
    elif manjesh=="":
        return redirect('/')
    elif 'token' in manjesh:
          
        return render(request,'about.html')
    else:
        return redirect('/')      

def coming(request):
    manjesh = request.COOKIES
    
    if not manjesh:
        return redirect('/')
    elif manjesh=="":
        return redirect('/')
    elif 'token' in manjesh:
          
        return render(request,'coming.html') 
    else:
        return redirect('/')
            

def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect("/")
    response.delete_cookie('token')
    return response

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
            encoded_token = jwt.encode({'id':hi.id}, "manjesh", algorithm='HS256')
            
            response = HttpResponseRedirect("/about")
            response.set_cookie('token', encoded_token)  
            # decoded = jwt.decode(encoded_token, "manjesh", algorithms='HS256')
            
            messages.success(request,'login successfull')
    
            return response

        else:
            messages.info(request,'Invalid credentials')
            return redirect('/login')

    else:
        return render(request,'login.html')        