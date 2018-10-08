from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rentals import views
# from django.contrib.auth.views import login
from django.contrib.auth import views as auth

urlpatterns = [
#Home page for public
	#Home Page
    url(r'^$', views.home, name='home'),	# '^$' is for / which is the first page

#Admin for modifying database from website
    #Admin
    url(r'^admin/', admin.site.urls),

#Management sites for data viewing
    #Main Login Page
    # url(r'^login/', views.login, name='login'),

    #Mangement login page
    url(r'^manage/login/', views.manage_login, name='manage_login'),
    #Home page
    url(r'^manage/', views.manage_home, name='manage_home'),

    #Vehicles
    url(r'^vehicles/', views.manage_vehicles, name='manage_vehicles'),
    #Individual with ID
    url(r'^vehicle/(\d+)/', views.vehicle_id, name='vehicle_id'),

    #Customers
    url(r'^customers/', views.manage_customers, name='manage_customers'),
    #Individual with ID
    url(r'^customer/(\d+)/', views.customer_id, name='customer_id'),

    #Order
    url(r'^orders/', views.manage_orders, name='manage_orders'),
    #Individual with ID
    url(r'^order/(\d+)/', views.order_id, name='order_id'),

    #Store
    url(r'^stores/', views.manage_stores, name='manage_stores'),
    #Individual with ID
    url(r'^store/(\d+)/', views.store_id, name='store_id'),
]
