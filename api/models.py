from django.db import models

# Create your models here.

class TouristSite(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    story=models.TextField(max_length=200,null=True,blank=True)
    photo=models.ImageField(upload_to="places_ph",null=True,blank=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    type=models.CharField(max_length=50,null=True,blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.type

class AirLine(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    poster=models.ImageField(upload_to="airlines_ph",null=True,blank=True)
    tickets=models.ManyToManyField(Ticket)

    def __str__(self):
        return self.name
    


class Hotel(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    H_photo=models.ImageField(upload_to="hotels_ph",null=True,blank=True)
    rate=models.IntegerField(null=True,blank=True)
    

    def __str__(self):
        return self.name

class TravelPlaceImages(models.Model):
    tp=models.CharField(max_length=50,null=True,blank=True)
    images=models.ImageField(upload_to="places_ph",null=True,blank=True)
    def __str__(self):
        return self.tp

class TravelPlace(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    story=models.TextField(max_length=200,null=True,blank=True)
    photo=models.ImageField(upload_to="places_ph",null=True,blank=True)
    photos=models.ManyToManyField(TravelPlaceImages)
    tourSites=models.ManyToManyField(TouristSite )
    hotels=models.ManyToManyField(Hotel)
    airlines=models.ManyToManyField(AirLine)
    date=models.DateField(null=True, blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    def __str__(self):
        return self.name
    






