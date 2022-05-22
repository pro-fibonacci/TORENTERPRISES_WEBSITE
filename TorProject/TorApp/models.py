
from unicodedata import name
from django.db import models

# Create your models here.
class Homepage(models. Model):
		Service_name = models.CharField(max_length=20, null=True)
		Service_details = models.CharField(max_length=2000, null=True)
		Benefit_head = models.CharField(max_length=20, null=True)
		Benefit_daetails = models.CharField(max_length=3000, null=True)
		Service2_name = models.CharField(max_length=20, null=True)
		Service2_details = models.CharField(max_length=2000, null=True)
		Benefit2_head = models.CharField(max_length=20, null=True)
		Benefit2_daetails = models.CharField(max_length=3000, null=True)
		Service3_name = models.CharField(max_length=20, null=True)
		Service3_details = models.CharField(max_length=2000, null=True)
		Benefit3_head = models.CharField(max_length=20, null=True)
		Benefit3_daetails = models.CharField(max_length=3000, null=True)
    
def __str__(self):
    return self.name 


class Goods(models. Model):
		Number= models.IntegerField(default=0, null=True, blank=True)
		General_name = models.CharField(max_length=200, null=True)
		Popular_name = models.CharField(max_length=200, null=True)
		Size = models.IntegerField(default=0, null=True, blank=True)
		Price= models.IntegerField(default=0, null=True, blank=True)
		Percent= models.IntegerField(default=0, null=True, blank=True)

def __str__(self):
    return self.name 

class contact(models. Model):
		full_name = models.CharField(max_length=3000, null=True)
		email = models.EmailField()
		desc = models.TextField()

def __str__(self):
    return self.name 


class About_us(models. Model):
		Storing = models.TextField()
		Supply = models.TextField()
		Retailing = models.TextField()

def __str__(self):
    return self.name 

class Faqing(models. Model):
		Faqs =  models.TextField()


def __str__(self):
    return self.name 

class Term(models. Model):
		term = models.TextField()
	

def __str__(self):
    return self.name 



class PrivacyP(models. Model):
		policy =  models.TextField()
	

def __str__(self):
    return self.name 
