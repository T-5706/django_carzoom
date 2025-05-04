from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book/<int:car_id>/', views.book_car, name='book_car'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('hyundai/', views.hyundai, name='hyundai'),
    path('xuv/', views.xuv, name='xuv'),
    path('honda/', views.honda, name='honda'),
    path('suv/', views.suv,name='suv'),
    path('pay/<int:car_id>/', views.initiate_payment, name='initiate_payment'),
    path('error/', views.error, name='error'),

]