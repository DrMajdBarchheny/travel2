from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from .util import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'index.html')
@api_view(['GET'])
def getPLaces(request):
    travel=TravelPlace.objects.all()
    serializer=TravelPlacesSerializer(travel,many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getPlace(request,pk):
    place=TravelPlace.objects.get(id=pk)
    serializer=TravelPlacesSerializer(place,many=False)
    return Response(serializer.data)

    
@api_view(['GET'])
def getSearch(request):
    query=request.query_params.get('q')
    if query is "":
        query="pppp"
        
    else:
        print('query : ',query)
        
    result=TravelPlace.objects.filter(Q(name__icontains=query)|Q(country__icontains=query))

    print(result)
    serializer=TravelPlacesSerializer(result,many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def getDate(request):
    query=request.query_params.get('q',None)
    if query is "":
        query="pppp"
        
    else:
        print('query : ',query)
    result=TravelPlace.objects.filter(date__icontains=query)
    serializer=TravelPlacesSerializer(result,many=True)
    return Response(serializer.data)


#for the tour site

@api_view(['GET'])
def getTourSites(request):
    sites = TouristSite.objects.all()
    serializer = TouristSiteSerializer(sites , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTourSite(request,pk):
    site=TouristSite.objects.get(id=pk)
    serializer=TouristSiteSerializer(site,many=False)
    return Response(serializer.data)


#for the Ticket

@api_view(['GET'])
def getTickets(request):
    tickets = TouristSite.objects.all()
    serializer = TicketSerializer(tickets , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTicket(request,pk):
    ticket=TouristSite.objects.get(id=pk)
    serializer=TicketSerializer(ticket,many=False)
    return Response(serializer.data)



#for the hotel

@api_view(['GET'])
def getHotels(request):
    hotels = TouristSite.objects.all()
    serializer = HotelSerializer(hotels , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getHotel(request,pk):
    hotel=TouristSite.objects.get(id=pk)
    serializer=HotelSerializer(hotel,many=False)
    return Response(serializer.data)




#for the hotel

@api_view(['GET'])
def getAirLines(request):
    airlines = AirLine.objects.all()
    serializer = AirLineSerializer(airlines , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAirLine(request,pk):
    airline=AirLine.objects.get(id=pk)
    serializer=AirLineSerializer(airline,many=False)
    return Response(serializer.data)


# @csrf_exempt
# def get_prices(request, number):
#     # Assuming 'number' corresponds to the 'price' field in your Ticket model
#     # and you want to find tickets with prices less than or equal to the input number
#     tickets = Ticket.objects.filter(price__lte=number)

#     response_data = []
#     for ticket in tickets:
#         # For each ticket, get the related AirLine information
#         airlines = ticket.airline_set.all()
#         for airline in airlines:
#             response_data.append({
#                 'ticket_type': ticket.type,
#                 'airline_name': airline.name,
#                 'airline_poster': airline.poster.url if airline.poster else None,
#              })

#     return JsonResponse(response_data, safe=False)

@api_view(['GET'])
def getPrice(request):
    query=request.query_params.get('q')
    # if query is "":
    #     query="pppp"
        
    # else:
    #     print('query : ',query)
    result=TravelPlace.objects.filter(price__lte=query)
    serializer=TravelPlacesSerializer(result,many=True)
    return Response(serializer.data)