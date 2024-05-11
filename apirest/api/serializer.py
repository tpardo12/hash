from rest_framework  import  serializers
from .models import HashKey


class HashSerializer (serializers.ModelSerializer):
    class Meta:
        model = HashKey
        fields = '__all__'