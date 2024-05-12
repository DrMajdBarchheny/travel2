# from rest_framework.response import Response
# from .models import *
# from .serializers import *
# def postsearch(request):
#     s=request.data
#     r=TravelPlace.objects.filter(name__contains=s)
    
#     return r
# def getserch(request):
#     # if request.method == "POST":
#     #    s =request.data
#     #    print(s)
#     #    r=TravelPlace.objects.filter(name__contains=s)
#     #    ss=SearchSerializer(r,many=True)
#     #    return Response(ss.data)
#     q=request.GET.get('q')
#     if q:
#         result = TravelPlace.objects.filter(name__contains=q)
    
#     else:
#         result=TravelPlace.objects.all()
    
#     serializer=SearchSerializer(result,many=True)
#     return Response(serializer.data)
    