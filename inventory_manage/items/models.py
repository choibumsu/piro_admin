from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=30, verbose_name="이름")
    tel = models.CharField(max_length=30, verbose_name="전화번호")
    address = models.CharField(max_length=100, verbose_name="주소")

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name="제품명")
    photo = models.ImageField(
        blank=True, upload_to="item/%Y/%m/%d", verbose_name="제품 사진")
    description = models.TextField(blank=True, verbose_name="제품 설명")
    price = models.IntegerField(verbose_name="가격")
    amount = models.IntegerField(verbose_name="남은 수량")
    customer = models.ForeignKey(
        'Customer', related_name='items', on_delete=models.CASCADE, verbose_name="거래처")

    def __str__(self):
        return self.name
