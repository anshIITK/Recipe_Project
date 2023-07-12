from django.shortcuts import render, redirect
from .models import *

# Create your views here.

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
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes/')

# Creating function to update already existing recipe.
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

