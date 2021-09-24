from rest_framework import serializers
<<<<<<< HEAD
<<<<<<< HEAD
from models import Livre
=======
from .models import Livre
>>>>>>> 49fd3c8b311a0d8a1bb0c12fff3851f63259fc89


class LivreSerializer(serializers.ModelSerializer):

     class Meta:
        model = Livre
        fields = ('id',
                  'titre',
                  'description',
                  'quantite',
<<<<<<< HEAD
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
=======
                  'genre'
                  )
>>>>>>> 49fd3c8b311a0d8a1bb0c12fff3851f63259fc89
