from django.urls import path
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.index, name="index"),
	path('about/', views.About, name="about"),
 	path('add_contact/', views.add_contact, name="add_contact"),
	path('contact/', views.Contact, name="contact"),
	path('price/', views.Price, name="price"),
	path('faq/', views.Faq, name="faq"),
	path('storage/', views.Storage, name="storage"),
	path('privacy/', views.Privacy, name="privacy"),
	path('terms/', views.Terms, name="terms"),

]