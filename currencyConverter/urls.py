from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('cv-admin/', views.AdminView, name='admin'),
	path('cv-admin/addCurrency/', views.addCurrency, name='addCurrency'),
	path('cv-admin/update/<country_id>/', views.update, name='update'),
	path("login/", views.Connexion, name='login'),
	path("logout/", views.disconnect, name='logout'),
	path("register/", views.Register.as_view(), name='register'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),

]
