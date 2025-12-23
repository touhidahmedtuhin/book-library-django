from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)


class Book(models.Model):
  title = models.CharField(max_length=50)
  rating = models.IntegerField(validators=[
    MinValueValidator(1),MaxValueValidator(5)
  ])
  author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="books")
  is_bestseller = models.BooleanField(default=False)
  slug = models.SlugField(default="",blank=True,null=False,unique=True)

  def get_absolute_url(self):
     return reverse("book_details", args=[self.slug])

  
  def __str__(self):
    return f"{self.title} by {self.author} (Rating: {self.rating}), Best Seller: {self.is_bestseller})"
  