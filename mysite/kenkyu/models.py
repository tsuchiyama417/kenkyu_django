from django.db import models

# Create your models here.
class Organism(models.Model):
    # id : INT(primary)
    org_id = models.IntegerField(primary_key=True)
    # 生物種の名前 : CHAR
    org_name = models.CharField(max_length=100)
    # 生物種の配列 : CHAR
    org_arr = models.CharField(max_length=1000)

# # Create your models here.
# class AminoVector(models.Model):
#     # id : INT(primary)
#     amino_id = models.IntegerField(primary_key=True)
#     # アミノ酸の名前 : CHAR
#     amino_name = models.CharField(max_length=1)
#     # アミノ酸のx,y,z座標 : FLOAT
#     amino_x = models.FloatField()
#     amino_y = models.FloatField()
#     amino_z = models.FloatField()
    