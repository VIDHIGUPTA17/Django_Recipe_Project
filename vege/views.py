from django.db import IntegrityError
from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import Receipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login_page/")
def receipes(request):
    print("hello world")
    if request.method=="POST":
        data=request.POST
        image=request.FILES.get('image')
        receipdes=data.get('receipdes')
        receipname=data.get('receipname')
        print(image)
        print(receipdes)
        print(receipname)
        Receipe.objects.create(image=image,receipdes=receipdes,receipname=receipname)
        return redirect('/receipes/')
    queryset=Receipe.objects.all()
    context={'receipes':queryset}
    return render(request,'receipe.html',context)

@login_required(login_url="/login_page/")
def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        image=request.FILES.get('image')
        receipdes=data.get('receipdes')
        receipname=data.get('receipname')
        queryset.receipname=receipname
        queryset.receipdes=receipdes
        if image:
            queryset.image=image
        queryset.save()   
        return redirect('/receipes/')

        # Receipe.objects.create(image=image,receipdes=receipdes,receipname=receipname)
        # return redirect('/receipes/')
    context={'receipes':queryset}

    return render(request,'update_receipe.html',context)

@login_required(login_url="/login_page/")
def delete_receipe(request,id):
    print(id)
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')
    # return HttpResponse("a")
        # return redirect('/receipes/')



def login_page(request):
    
        
        if request.method == "POST":
              print(request.POST)
              username = request.POST.get("username")
              password = request.POST.get("password")

              if not username or not password:
                  messages.error(request, "All fields are required.")
                  return redirect("/login_page/")
        

              user=User.objects.filter(username=username)
              if not user.exists():
                  print("already exiat")
                  messages.error(request,"invalid usernamer")
                  return redirect("/login_page/")
              
              user= authenticate(username=username , password=password)
              if user is None:
                  messages.error(request,"invalid password")
                  return redirect("/login_page/")
              
              else:
                  login(request,user)
                  return redirect("/receipes/")
              
                  

        



        # try:
        #     user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username)
        #     user.set_password(password)
        #     user.save()
        #     messages.success(request, "Account created successfully.")
        #     return redirect("/login_page/")
        # except IntegrityError:
        #     messages.error(request, "Username already exists.")
        #     return redirect("/register/")


    # pass
        return render(request,'login.html')


def logout_page(request):
    logout(request)
    return redirect("/login_page/")


def register(request):
    if request.method == "POST":
        print(request.POST)
        first_name = request.POST.get("first-name")
        last_name = request.POST.get("last-name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        

        

        if not first_name or not last_name or not username or not password:
            messages.error(request, "All fields are required.")
            return redirect("/register/")
        # user=User.objects.filter(username=username)
        # if user.exists:
        #     print("already exiat")
        #     messages.info(request,"Already exsist user")


        try:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username)
            user.set_password(password)
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect("/login_page/")
        except IntegrityError:
            messages.error(request, "Username already exists.")
            return redirect("/register/")
    
    return render(request, 'register.html')



