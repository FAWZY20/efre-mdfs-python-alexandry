from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

<<<<<<< HEAD
<<<<<<< HEAD
from models import Livre
from serializers import LivreSerializer
=======
from .models import Livre
from efreiAPI.serializers import LivreSerializer
>>>>>>> 49fd3c8b311a0d8a1bb0c12fff3851f63259fc89
from rest_framework.decorators import api_view


@api_view(['GET', 'DELETE'])
def Livre_list_published(request):
    if request.method == 'GET':
        livres = Livre.objects.all()
        livre_serializer = LivreSerializer(livres, many=True)
        return JsonResponse(livre_serializer.data, safe=False)

<<<<<<< HEAD
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

=======
>>>>>>> 49fd3c8b311a0d8a1bb0c12fff3851f63259fc89

@api_view(['POST'])
def add_livre(request):
    if request.method == 'POST':
<<<<<<< HEAD
>>>>>>> pull
=======
>>>>>>> 49fd3c8b311a0d8a1bb0c12fff3851f63259fc89
        livre_data = JSONParser().parse(request)
        livre_serializer = LivreSerializer(data=livre_data)
        if livre_serializer.is_valid():
            livre_serializer.save()
            return JsonResponse(livre_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(livre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD
<<<<<<< HEAD
    elif request.method == 'DELETE':
        count = Livre.objects.all().delete()
        return JsonResponse({'message': '{} Livres were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
=======
>>>>>>> 49fd3c8b311a0d8a1bb0c12fff3851f63259fc89

@api_view(['PUT'])
def update_livre(request, pk):
    try:

        livre = Livre.objects.get(pk=pk)

    except Tutorial.DoesNotExist:

        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':

<<<<<<< HEAD
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
=======
>>>>>>> 49fd3c8b311a0d8a1bb0c12fff3851f63259fc89
        livre_data = JSONParser().parse(request)
        livre_serializer = LivreSerializer(livre, data=livre_data)
        if livre_serializer.is_valid():
            livre_serializer.save()
            return JsonResponse(livre_serializer.data)
        return JsonResponse(livre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD
<<<<<<< HEAD
    elif request.method == 'DELETE':
        livre.delete()
        return JsonResponse({'message': 'Livre was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
=======
>>>>>>> 49fd3c8b311a0d8a1bb0c12fff3851f63259fc89

@api_view(['DELETE'])
def delete_livre(request, pk):

    try:

<<<<<<< HEAD
    if request.method == 'GET':
        livres_serializer = LivreSerializer(livres, many=True)
        return JsonResponse(livres_serializer.data, safe=False)
=======

@api_view(['DELETE'])
def delete_livre(request, pk):

    try:

        livre = Livre.objects.get(pk=pk)

    except Tutorial.DoesNotExist:
=======
        livre = Livre.objects.get(pk=pk)

    except Livre.DoesNotExist:
>>>>>>> 49fd3c8b311a0d8a1bb0c12fff3851f63259fc89

        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':

        livre.delete()
<<<<<<< HEAD
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
>>>>>>> pull
=======
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
>>>>>>> 49fd3c8b311a0d8a1bb0c12fff3851f63259fc89
