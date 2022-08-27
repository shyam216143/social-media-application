from email.mime import image
from re import I
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib import messages
@login_required(login_url='signin')
def home(request):
    return render(request,"index.html")
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if len(username) == 0:
            messages.info(request,"Username is required,")
        elif len(firstname) == 0:
            messages.info(request,"firstname is required,")

        elif len(lastname) == 0:
            messages.info(request,"lastname is required,")
        elif len(email) == 0:
            messages.info(request,"email is required,")
        elif len(password1) == 0:
            messages.info(request,"password is required,please enter password")
        elif len(password2) == 0:
            messages.info(request,"Confirmed password is required to confirm")

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists, Please Use another one')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists, Please use Another Email Addresss')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,first_name = firstname,last_name=lastname, email=email, password=password1 )
                user.save()

                #log user in and redirect to settings page
                userlogin = auth.authenticate(username=username, password=password1)
                auth.login(request,userlogin)
               

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Password Not Matching, please enter correct password')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')
    


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request,"Username or Password is Invalid")  
            return redirect('signin')  
    else:
        return render(request, "signin.html")


@login_required(login_url='signin')
def settings(request):
    user_profile = profile.objects.get(user=request.user)
    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.profile_img
            bio = request.POST['bio']
            location = request.POST['address']
            
            user_profile.profile_img = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        if request.FILES.get('image') != None:    
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['address']   
            user_profile.profile_img = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        return redirect('settings')




    return render(request, "setting.html" ,{"user_profile":user_profile})

def example(request):
    return render(request, "signin.html") 

@login_required(login_url='signin')
def signout(request):
    auth.logout(request)
    return redirect('signin')