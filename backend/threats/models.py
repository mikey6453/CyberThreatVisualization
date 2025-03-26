from django.db import models

# Create your models here.
from django.db import models

class CyberAttack(models.Model):
    country = models.CharField(max_length=100)
    year = models.IntegerField()
    attack_type = models.CharField(max_length=100)
    target_industry = models.CharField(max_length=100)
    financial_loss_million = models.FloatField()
    affected_users = models.BigIntegerField()
    attack_source = models.CharField(max_length=100)
    vulnerability_type = models.CharField(max_length=100)
    defense_mechanism = models.CharField(max_length=100)
    resolution_time_hours = models.IntegerField()

    def __str__(self):
        return f"{self.country} - {self.year} - {self.attack_type}"
