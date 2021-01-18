from rest_framework import serializers
from canditate.models import Candidate, Vote

class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = ['id','first_name', 'last_name', 'picture','political_party', 'date_add', 'date_updated','votes']


class VoteSerializer(serializers.ModelSerializer):

    candidates = CandidateSerializer(many=True)

    class Meta:
        model = Vote
        fields = ['id','vote_title', 'vote_description','candidates', 'voters', 'start_date', 'end_date']

