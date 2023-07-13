from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model deals with Data
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank= True)
    recipe_name = models.CharField(max_length=50)
    recipe_desc = models.TextField()
    recipe_img = models.ImageField(upload_to="recipeImages")

