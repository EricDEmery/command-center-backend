from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    epic_id = serializers.CharField()  # Add the 'epic_id' field

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'epic_id')  # Include 'epic_id' here
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    epic_id = serializers.CharField(source='author.epic_id', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at', 'epic_id']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        validated_data['epic_id'] = self.context['request'].user.epic_id
        return super().create(validated_data)
