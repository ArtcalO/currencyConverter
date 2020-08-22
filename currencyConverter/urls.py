from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('cv-admin/', views.AdminView, name='admin'),
	path('cv-admin/addCurency/', views.AddCurrencyView, name='addCurency'),
	path('cv-admin/addCountry/', views.AddCountryView, name='addCountry'),
	path('cv-admin/update/<currency_id>/', views.update, name='update'),
	path('cv-admin/delete/<currency_id>/', views.delete, name='delete'),
	path("login/", views.Connexion, name='login'),
	path("logout/", views.disconnect, name='logout'),
	path("register/", views.Register.as_view(), name='register'),
	path("display/", views.display, name='display'),

]