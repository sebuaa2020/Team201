from django.db import models

class Room(models.Model):
    roomNo = models.CharField(max_length=50, primary_key=True)

class Robot(models.Model):
    robotNo = models.CharField(max_length=50, primary_key=True)
    robotState = models.IntegerField()
    robotIdx_x = models.FloatField()
    robotIdx_y = models.FloatField()
    robotPower = models.IntegerField()

class Goods(models.Model):
    goodsNo = models.CharField(max_length=50, primary_key=True)
    goodsName = models.CharField(max_length=50)
    goodsIdx_x = models.FloatField()
    goodsIdx_y = models.FloatField()

class Instruction(models.Model):
    insNo = models.CharField(max_length=50, primary_key=True)
    insType = models.IntegerField()
    insRoomNo = models.ForeignKey(Room, on_delete=models.CASCADE)
    insGoodsNo = models.ForeignKey(Goods, on_delete=models.CASCADE)
