from django.shortcuts import render
from .models import *

# Create your views here.

def About(request): 
    about = About_us.objects.all()
    context = {'about': about}
    return render(request, 'pages/about.html', context)

def Contact(request):
     context = {}
     return render(request, 'pages/contact.html', context)

def add_contact(request):
     print("form submitted")
     full_name = request.POST['full_name']
     email = request.POST['email']
     desc = request.POST['desc']
     contact_details = contact (full_name=full_name, email=email, desc=desc,)
     contact_details.save()
     return render(request, 'pages/contact.html')

def index(request):
      home = Homepage.objects.all()
      context = {"home": home}
      return render(request, 'pages/index.html', context)
  
def Price(request):
      goods = Goods.objects.all()
      context = {"goods":  goods}
      return render(request, 'pages/price.html', context)
  
def Faq(request):
      faq = Faqing.objects.all()
      context = {'faq' : faq}
      return render(request, 'pages/faq.html', context)
  
def Privacy(request):
      policy = PrivacyP.objects.all()
      context = {'policy' : policy}
      return render(request, 'pages/privacy.html', context)

def Storage(request):
      context = {}
      return render(request, 'pages/storage.html', context)
  
def Terms(request):
      term = Term.objects.all()
      context = {'term' : term}
      return render(request, 'pages/terms.html', context)

