from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BeerType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.typename
    
    class Meta:
        db_table='beertype'
        verbose_name_plural='beertypes'

class Beer(models.Model):
    beername=models.CharField(max_length=255)
    beertype=models.ForeignKey(BeerType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    beerprice=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    beerentrydate=models.DateField()
    beerurl=models.URLField(null=True, blank=True)
    beerdescription=models.TextField()

    def memberdiscount(self):
        discountpercent=.05
        return float(self.beerprice) * discountpercent

    def __str__(self):
        return self.beername
    
    class Meta:
        db_table='beer'
        verbose_name_plural='beers'

class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    beer=models.ForeignKey(Beer, on_delete=models.CASCADE)
    user=models.ManyToManyField(User)
    reviewrating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle
    
    class Meta:
        db_table='review'
        verbose_name_plural='reviews'