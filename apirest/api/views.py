
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import serializers
from rest_framework import status
from .models import HashKey
from .serializer import HashSerializer
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by ids': '/?ids=ids',
        'Add': '/register',
    
    }
 
    return Response(api_urls)


@api_view(['POST'])
def add_items(request):
    hash = HashSerializer(data=request.data)
    
 
    if hash.is_valid():
        hash.save()
        return Response(hash.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def check(request):
    info = request.data
    id = info['ids']
    key = info['hash']
    hash = HashKey.objects.get(ids = id)
    serializer = HashSerializer(hash, many = False)
    sarializerData = serializer.data
    if (sarializerData['hash'] == key):
        return Response({"result" : True})
    else:
        return Response({"result" : False})
    
    
@api_view(['POST'])
def checkMultiple(request):
    info = request.data
    eList = []
    for i in info:
        id = i['ids']
        key = i['hash']
        hash = HashKey.objects.get(ids = id)
        serializer = HashSerializer(hash, many = False)
        sarializerData = serializer.data
        if (sarializerData['hash'] != key):
            eList.append(id)
    return Response(eList)
        
   
    
    
