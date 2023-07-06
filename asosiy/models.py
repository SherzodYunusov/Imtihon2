from django.db import models
from django.contrib.auth.models import User

class Suv(models.Model):
    brend = models.CharField(max_length=50)
    narx = models.IntegerField()
    litr = models.PositiveSmallIntegerField()
    batafsil = models.CharField(max_length=50)


class Mijoz(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.IntegerField()
    manzil = models.CharField(max_length=50)
    qarz = models.PositiveSmallIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Admin(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.IntegerField()
    ish_vaqt = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Haydovchi(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.IntegerField()
    kiritilgan_sana = models.DateField(auto_now_add=True)

class Buyurtma(models.Model):
    miqdor = models.CharField(max_length=50)
    umumiy_summa = models.IntegerField()
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE)
    suv_id = models.ForeignKey(Suv, on_delete=models.CASCADE)
    haydovchi_id = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)
    mijoz_id = models.ForeignKey(Mijoz, on_delete=models.CASCADE)



# Create your models here.
