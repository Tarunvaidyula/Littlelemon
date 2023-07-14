from django.db import models

# Create your models here.

class category(models.Model):
    slug=models.SlugField()
    title=models.CharField(max_length=255, db_index=True)
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name
    
class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name
  
class MenuItem(models.Model):
    title=models.CharField(max_length=255, db_index=True)    
    price=models.DecimalField(max_digits=6, decimal_places=2,db_index=True)
    featured=models.BooleanField(db_index=True)
    Category=models.ForeignKey(category,on_delete=models.PROTECT)