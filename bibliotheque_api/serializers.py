from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ProfilUtilisateur

class RegisterSerializer(serializers.ModelSerializer):
    departement = serializers.CharField(write_only=True, required=True)
    filiere = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'departement', 'filiere']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Un utilisateur avec cet email existe déjà.")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Ce nom d'utilisateur est déjà pris.")
        return value

    def create(self, validated_data):
        departement = validated_data.pop('departement')
        filiere = validated_data.pop('filiere')
        user = User.objects.create_user(**validated_data)
        ProfilUtilisateur.objects.create(user=user, departement=departement, filiere=filiere)  # type: ignore
        return user
