from django.db import models

# Create your models here.
class Bills(models.Model):
    Bill_Number=models.CharField(max_length=5)
    Amount=models.IntegerField()
    def __str__(self):
        return f"{self.Amount}"