from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(
            student_id = validated_data['student_id'],
            username = validated_data['username'],
            password = validated_data['password'],
            password_check = validated_data['password_check']
        )
        return user