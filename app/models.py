from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # resumeUrl = models.CharField(max_length=200)
    # targetSalaryMin = models.IntegerField(required=True)
    # targetSalaryMax = models.IntegerField()
    # topBenefits = models.CharField(max_length=200, required=True)  # Comma-separated string array
    # certifications = models.CharField(max_length=200)  # Comma-separated string array
    # topTraits = models.CharField(max_length=200, required=True)  # Comma-separated string array
    # additionalInfo = models.TextField()
