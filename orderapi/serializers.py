
from rest_framework import serializers
from .models import BookOrder

class BookOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookOrder
        fields = '__all__'