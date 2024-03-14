from rest_framework import serializers
from ducks.models import Duck

class DuckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duck
        fields =('id', 'name','age','location', 'image')
