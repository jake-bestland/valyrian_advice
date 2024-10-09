from django.db import models

# Create your models here.
# class AdviceSlip(models.Model):
#     id = models.IntegerField()
#     advice = models.CharField(max_length=200)

#     def __str__(self):
#         return self.advice
    
class CombinedData(models.Model):
    advice = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)