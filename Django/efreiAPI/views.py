from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Livre
from efreiAPI.serializers import LivreSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'DELETE'])
def Livre_list_published(request):
    if request.method == 'GET':
        livres = Livre.objects.all()
        livre_serializer = LivreSerializer(livres, many=True)
        return JsonResponse(livre_serializer.data, safe=False)


# @api_view(['POST'])
# def add_livre():
#    if request.method == 'POST':
#        return None


# @api_view(['PUT'])
# def add_livre():
#    if request.method == 'PUT':
#        return None


@api_view(['DELETE'])
def delete_livre(request, pk):

    try:

        livre = Livre.objects.get(pk=pk)

    except Tutorial.DoesNotExist:

        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        
        livre.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
