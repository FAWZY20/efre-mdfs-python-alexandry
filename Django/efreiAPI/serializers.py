from rest_framework import serializers
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
