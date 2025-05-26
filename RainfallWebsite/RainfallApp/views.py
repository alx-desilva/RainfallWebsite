from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from RainfallApp.models import RainfallList
import logging

# Create your views here.
from django.http import HttpResponse

def index(request):
    if request.user.is_authenticated:
        return redirect('RainfallApp:use')
    else:
        return render(request, 'RainfallApp/homepage.html')

def calculation_page(request):
    print(f"calculation_page called with method: {request.method}")
    context = {}
    if request.method == 'GET':
        equation_id = request.GET.get('equation_id')

        if equation_id:
            # User clicked on an old equation
            try:
                equation = RainfallList.objects.get(id=equation_id, user=request.user)
                context['selected_equation'] = equation
            except RainfallList.DoesNotExist:
                context['error'] = "Equation not found."
        
        
        equations = RainfallList.objects.filter(user=request.user).order_by("-id")
        context['equations_list'] = equations
        return render(request, 'RainfallApp/calculation_page.html', context=context)
    
    elif request.method == 'POST':
        if request.user.is_authenticated:
            title = request.POST['Name']
            location = request.POST['location']
            perc = request.POST['Percipitation']
            area = request.POST['area']
            coef = request.POST['Coefficient']
            user = request.user

            Vrunoff = float(perc) * float(area) * float(coef)

            rainfall = RainfallList(Title=title, Location=location, VolumeOfRunoff=Vrunoff, Precipitation=perc, Area=area, SurfaceCoefficient=coef, user=user)
            rainfall.save()
            
            context['vrunoff'] = Vrunoff
            
            context['equations_list'] = RainfallList.objects.filter(user=request.user).order_by("-id")


            return render(request, 'RainfallApp/calculation_page.html', context=context)
    

def login_request(request):
   context = {}

   if request.method == "POST":
      username = request.POST['username']
      password = request.POST['psw']
      user = authenticate(username=username, password=password)
      if user is not None:
         login(request, user)
         return redirect('RainfallApp:use')
      else:
         return render(request, 'RainfallApp/user_login.html', context)
   else:
      return render(request, 'RainfallApp/user_login.html', context)


def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'RainfallApp/user_registration.html', context)
    elif request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['psw']
        passwordConf = request.POST['psw2']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            #logger.debug("{} is new user".format(username))
            print("Im sigma")
        if not user_exist and password == passwordConf:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("RainfallApp:use")
        else:
            context = {'error_message': 'Username Taken or Passwords Dont Match'}
            return render(request, 'RainfallApp/user_registration.html', context)
        

def logout_request(request):
    print("Log out the user `{}`".format(request.user.username))

    logout(request)
   
    return redirect('RainfallApp:index')

"""def create_equation(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'RainfallApp/create_equation.html', context)
    
    elif request.method == 'POST':
        if request.user.is_authenticated:
            title = request.POST['Name']
            location = request.POST['location']
            perc = request.POST['Percipitation']
            area = request.POST['area']
            coef = request.POST['Coefficient']
            user = request.user

            Vrunoff = float(perc) * float(area) * float(coef)

            rainfall = RainfallList(Title=title, Location=location, VolumeOfRunoff=Vrunoff, Precipitation=perc, Area=area, SurfaceCoefficient=coef, user=user)
            rainfall.save()
            
            context['vrunoff'] = Vrunoff
            
            context['equations_list'] = RainfallList.objects.filter(user=request.user).order_by("-id")


            return render(request, 'RainfallApp/calculation_page.html', context=context)
"""
    