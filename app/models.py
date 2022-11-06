from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    middle_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    picture_url = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(
        max_length=20, blank=True, null=True
    )  # , blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + " (" + str(self.id) + ")"


class Employee(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)
    resumeUrl = models.CharField(max_length=200, blank=True, null=True)
    # targetSalaryMin = models.IntegerField(required=True)
    # targetSalaryMax = models.IntegerField()
    # topBenefits = models.CharField(max_length=200, required=True)  # Comma-separated string array
    # certifications = models.CharField(max_length=200)  # Comma-separated string array
    # topTraits = models.CharField(max_length=200, required=True)  # Comma-separated string array
    # additionalInfo = models.TextField()
