from rest_framework import serializers
from elector.models import Elector

class ElectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Elector
        fields = ['elector_id', 'first_name', 'last_name', 'front_picture', 'sexe', 'has_vote', 'candidate_id', 'date_of_issuance',
                  'date_of_expire']