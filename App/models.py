from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Driver(models.Model):
  fname = models.CharField(max_length=200, blank=True, null=True)
  tel = models.CharField(max_length=200, blank=True, null=True)
  car = models.CharField(max_length=200, blank=True, null=True)
  
  def __str__(self):
    return f"Name: {self.fname} => Car: {self.car} => Phone: {self.tel}"
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    fname = models.CharField(max_length=50, default=0)
    lname = models.CharField(max_length=50, default=0)
    address = models.CharField(max_length=50, default=0)
    room_no = models.CharField(max_length=50, default=0)
    night = models.IntegerField(default='1')
    rrr = models.CharField(max_length=15, default=0)
    lodgeIn = models.CharField(max_length=50, default=0)
    lodgeOut = models.CharField(max_length=50, default=0)
    adult = models.IntegerField(default=1)
    children = models.IntegerField(default=0)
    dob = models.CharField(max_length=50, default=0)
    car = models.IntegerField(default=0)
    meansOfId = models.CharField(max_length=200, blank=True, null=True)
    idNumber = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=200, blank=True, null=True)
    pick_up_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True, related_name='pick_up_driver')
    drop_off_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True, related_name='drop_off_driver')
    price = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.fname

class History(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
  history = models.CharField(max_length=200, blank=True, null=True)
  
  def __str__(self):
        return self.customer

class Category(models.Model):
    category = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.category

    def serialize(self):
        return {
            "id": self.pk,
            "category": self.category
        }
        
class Room(models.Model):
  roomName = models.CharField(max_length=50, blank=True, null=True)
  price = models.IntegerField()
  catg = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
  img_url = models.CharField(max_length=200, blank=True, null=True)
  
  def __str__(self):
    return self.roomName
  
  def serialize(self):
        return {
          "id": self.pk,
          "roomName": self.roomName,
          "price": self.price,
          "catg": self.catg.category,
          "img_url": self.img_url,
        }
  
class  Account(models.Model):
  bank_name = models.CharField(max_length=100, blank=True, null=True)
  
  acc_name = models.CharField(max_length=100, blank=True, null=True)
  
  acc_no = models.CharField(max_length=100, blank=True, null=True)
  
  def serialize(self):
    return {
      "id": self.pk,
      "bank_name": self.bank_name,
      "acc_name": self.acc_name,
      "acc_no": self.acc_no,
    }

  def __str__(self):
    return self.acc_no

  # def __str__(self):
  #   return f"Bank Name: {self.bank_name} => Acc. Number: {self.acc_no} => Acc. Name: {self.acc_name}"
  
class HotelConfig(models.Model):
  name = models.CharField(max_length=100, blank=True, null=True)
  customer_care_no = models.CharField(max_length=100, blank=True, null=True)
  address = models.CharField(max_length=100, blank=True, null=True)
  email = models.CharField(max_length=100, blank=True, null=True)
  parking_charge = models.CharField(max_length=100, blank=True, null=True)

  def __str__(self):
    return self.name