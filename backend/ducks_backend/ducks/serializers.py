from rest_framework import serializers
from ducks.models import Duck

class DuckSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = Duck
        fields =('id', 'name','age','location', 'image')
