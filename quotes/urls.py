from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('about.html', views.about, name="about"),
	path('faq.html', views.faq, name="faq"),
	path('add_stock.html', views.add_stock, name="add_stock"),
	path('delete/<stock_id>', views.delete, name="delete"),
	path('delete_<stock', views.delete_stock, name="delete_stock")

]
