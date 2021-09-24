from rest_framework import serializers
<<<<<<< HEAD
from models import Livre


class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = ('titre',
                  'description',
                  'quantite',
                  'genre')
=======
from .models import Livre


class LivreSerializer(serializers.ModelSerializer):

     class Meta:
        model = Livre
        fields = ('id',
                  'titre',
                  'description',
                  'quantite',
                  'genre'
                  )
>>>>>>> pull
