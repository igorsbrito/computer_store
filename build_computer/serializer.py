from rest_framework import serializers
from .models import Computer


class ComputerSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='belong.full_name', read_only=True)
    owner_email = serializers.CharField(source='belong.email', read_only=True)

    class Meta:
        model = Computer
        fields = ['mother_board', 'cpu', 'ram_memory', 'video_card', 'created_date', 'owner_name', 'owner_email']
