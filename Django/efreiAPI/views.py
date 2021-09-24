from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

<<<<<<< HEAD
from models import Livre
from serializers import LivreSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def livre_list(request):
    if request.method == 'GET':
        livres = Livre.objects.all()

        titre = request.query_params.get('titre', None)
        if titre is not None:
            livres = livres.filter(titre__icontains=titre)

        livre_serializer = LivreSerializer(livres, many=True)
        return JsonResponse(livre_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
=======
from .models import Livre
from efreiAPI.serializers import LivreSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'DELETE'])
def Livre_list_published(request):
    if request.method == 'GET':
        livres = Livre.objects.all()
        livre_serializer = LivreSerializer(livres, many=True)
        return JsonResponse(livre_serializer.data, safe=False)


@api_view(['POST'])
def add_livre(request):
    if request.method == 'POST':
>>>>>>> pull
        livre_data = JSONParser().parse(request)
        livre_serializer = LivreSerializer(data=livre_data)
        if livre_serializer.is_valid():
            livre_serializer.save()
            return JsonResponse(livre_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(livre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD
    elif request.method == 'DELETE':
        count = Livre.objects.all().delete()
        return JsonResponse({'message': '{} Livres were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def livre_detail(request, pk):
    try:
        livre = Livre.objects.get(pk=pk)
    except Livre.DoesNotExist:
        return JsonResponse({'message': 'The livre does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        livre_serializer = LivreSerializer(livre)
        return JsonResponse(livre_serializer.data)

    elif request.method == 'PUT':
=======

@api_view(['PUT'])
def update_livre(request, pk):
    try:

        livre = Livre.objects.get(pk=pk)

    except Tutorial.DoesNotExist:

        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':

>>>>>>> pull
        livre_data = JSONParser().parse(request)
        livre_serializer = LivreSerializer(livre, data=livre_data)
        if livre_serializer.is_valid():
            livre_serializer.save()
            return JsonResponse(livre_serializer.data)
        return JsonResponse(livre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD
    elif request.method == 'DELETE':
        livre.delete()
        return JsonResponse({'message': 'Livre was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def livre_list_published(request):
    livres = Livre.objects.filter(published=True)

    if request.method == 'GET':
        livres_serializer = LivreSerializer(livres, many=True)
        return JsonResponse(livres_serializer.data, safe=False)
=======

@api_view(['DELETE'])
def delete_livre(request, pk):

    try:

        livre = Livre.objects.get(pk=pk)

    except Tutorial.DoesNotExist:

        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':

        livre.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
>>>>>>> pull
