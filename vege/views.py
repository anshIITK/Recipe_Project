from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url= '/login/')
def recipes(request):
    if request.method == "POST":
        data = request.POST #for text data
        recipe_img = request.FILES.get('recipe_img') #for image data
        recipe_name = data.get("recipe_name")
        recipe_desc = data.get("recipe_desc")
        
        # Saving data into our Recipe Model
        Recipe.objects.create(
            recipe_img = recipe_img,
            recipe_name = recipe_name,
            recipe_desc = recipe_desc
        )
        return redirect('/recipes/') 
    
    # Getting all the objects into a variable "queryset"
    queryset = Recipe.objects.all()

    # If request is of Search type then filter out all recipes containing that name.
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    # "context" is used to send the data from backend to frontend.
    context = {'recipes': queryset }
    return render(request, "recipes.html", context)


# Creating function to delete recipe using request and the id of the item.
@login_required(login_url= '/login/')
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes/')

# Creating function to update already existing recipe.
@login_required(login_url= '/login/')
def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        recipe_img = request.FILES.get('recipe_img') #for image data
        recipe_name = data.get("recipe_name")
        recipe_desc = data.get("recipe_desc")

        queryset.recipe_name = recipe_name
        queryset.recipe_desc = recipe_desc
        if recipe_img:
            queryset.recipe_img = recipe_img
        
        queryset.save()
        return redirect('/recipes/')
    # rendering the context to the upate_recipes page.
    context = {'recipe': queryset }
    return render(request, "update_recipes.html", context)



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid username")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login/')
        
        else:
            login(request, user) # Allowing the user to stay login and maintain session
            return redirect('/recipes/')

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)  # To store password in encrypted form
        user.save()

        messages.info(request, "Account created Successfully")

    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')

