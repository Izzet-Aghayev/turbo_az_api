from encodings.punycode import T
from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator,
)

from core.utils.models import TrackingModel
from . import (
    MILEAGE_CHOICE,
    CURRENCY_CHOICES,
    TRANSMISSION_CHOICES,
    OWNER_CHOICES,
    NUMBER_OF_SEATS_CHOICES,
)


class Brand(models.Model):
    name = models.CharField(max_length=50)


class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='car_models')
    name = models.CharField(max_length=50)


class RoofType(models.Model):
    name = models.CharField(max_length=50)


class Color(models.Model):
    name = models.CharField(max_length=50)


class FuelType(models.Model):
    name = models.CharField(max_length=50)


class GearBox(models.Model):
    name = models.CharField(max_length=50)


class EngineCapacity(models.Model):
    volume = models.CharField(max_length=50)


class ForCountry(models.Model):
    name = models.CharField(max_length=50)


class CarSupply(models.Model):
    name = models.CharField(max_length=50)



class Announcement(TrackingModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='announcements')
    CarModel = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='announcements')
    RoofType = models.ForeignKey(RoofType, on_delete=models.CASCADE, related_name='announcements')
    Color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='announcements')
    FuelType = models.ForeignKey(FuelType, on_delete=models.CASCADE, related_name='announcements')
    GearBox = models.ForeignKey(GearBox, on_delete=models.CASCADE, related_name='announcements')
    EngineCapacity = models.ForeignKey(EngineCapacity, on_delete=models.CASCADE, related_name='announcements')
    ForCountry = models.ForeignKey(ForCountry, on_delete=models.CASCADE, related_name='announcements')

    car_supply = models.ManyToManyField(CarSupply, related_name='announcements')

    mileage_type = models.CharField(max_length=10, choices=MILEAGE_CHOICE)
    currency_type = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    transmission_type = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES)
    owner_type = models.CharField(max_length=10, choices=OWNER_CHOICES)
    number_of_seats = models.CharField(max_length=10, choices=NUMBER_OF_SEATS_CHOICES, null=True, blank=True)

    is_crashed = models.BooleanField(default=False) # Vuruğu var
    is_damaged = models.BooleanField(default=False) # Qəzalı və ya ehtiyat hissələr üçün
    is_new = models.BooleanField(default=False)     # Yeni deyil
    is_colored = models.BooleanField(default=False) # Rənglənib

    with_credit = models.BooleanField(default=True)
    barter = models.BooleanField(default=True)
    
    vin_code = models.CharField(max_length=17, validators=[MinLengthValidator(17)])
    info = models.TextField(null=True, blank=True)

    mileage = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    price = models.DecimalField(max_digits=8, decimal_places=0)

    released_date = models.DateField()
    engine_power = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5000)])


class AnnouncementImage(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='announcements')
