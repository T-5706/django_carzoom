from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('car_details/', views.car_details, name='car_details'),
    path('suv/', views.suv,name='suv'),
    path('book/<int:car_id>/', views.book_car, name='book_car'),
    path('my-bookings/', views.my_bookings, name='my_bookings')


] 