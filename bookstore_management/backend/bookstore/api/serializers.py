from rest_framework import serializers
from .models import BookStoreModel

class BookStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStoreModel
        fields = '__all__'
        
# https://www.django-rest-framework.org/tutorial/1-serialization/