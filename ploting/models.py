from django.db import models

# Create your models here.




class Initial_Contact(models.Model):
     name = models.CharField(max_length=256)
     Relative = models.CharField(max_length=30)
     Owner = models.CharField(max_length=30)
     def __str__(self):
        return self.name



class Plot(models.Model):
    name = models.CharField(max_length=30)
    initial_information = models.ImageField(upload_to='initial_information')
    INITIAL_FEEDBACK = (
        ('INTERESTED', 'interested'),
        ('NOT INTERESTED', 'not interested'),
    )
    initial_feedback = models.CharField(max_length=60, choices=INITIAL_FEEDBACK)
    initial_contact = models.OneToOneField(
        Initial_Contact,
        on_delete=models.CASCADE,
    )
    agreement = models.ImageField(upload_to='agreement')
    first_payment_by_cheque = models.BooleanField(default=False)
    second_payment_by_cheque = models.BooleanField(default=False)
    third_payment_by_cheque = models.BooleanField(default=False)
    def __str__(self):
        return self.name



