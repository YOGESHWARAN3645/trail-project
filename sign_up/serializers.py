from rest_framework import serializers
from .models import user_details

class user_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_details
        fields = ('id','username','password','email')
