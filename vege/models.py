from django.db import models

# Create your models here.
# Model deals with Data
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    recipe_desc = models.TextField()
    recipe_img = models.ImageField(upload_to="recipeImages")

