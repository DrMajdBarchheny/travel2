from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('api/',views.getPLaces,name="places"),
    path('search/',views.getSearch,name="Search"),
    path('date/',views.getDate,name="date"),
    path('place/<str:pk>',views.getPlace,name="place"),
   # path('get_prices/<int:number>/', views.get_prices, name='get_prices'),
    path('price/',views.getPrice,name="price"),

    path('sites/',views.getTourSites,name="getTourSites"),
    path('sites/<str:pk>',views.getTourSite,name="getTourSite"),
    path('tickets/',views.getTickets,name="getTickets"),
    path('tickets/<str:pk>',views.getTicket,name="getTicket"),

    path('hotels/',views.getHotels,name="getHotels"),
    path('hotels/<str:pk>',views.getHotel,name="getHotel"),

    path('airlines/',views.getAirLines,name="getAirLines"),
    path('airlines/<str:pk>',views.getAirLine,name="getAirLine"),
]