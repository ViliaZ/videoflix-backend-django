from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    confirmed_email = serializers.EmailField(write_only=True)  # Neues Feld für die bestätigte E-Mail

    class Meta: 
        model = User
        fields = ['username', 'last_name', 'first_name', 'id', 'email', 'password', 'confirmed_email']
        extra_kwargs = {
            'password': {'write_only': True},  # Das Passwort sollte nur zum Erstellen verwendet werden
        }
   
   #POST
    def create(self, validated_data):
        email = validated_data.get('email')
        confirmed_email = validated_data.pop('confirmed_email')  # cut this field from validated_data to not be saved
        if email != confirmed_email:
            raise serializers.ValidationError('Die E-Mail-Adressen stimmen nicht überein.')

        existing_user = User.objects.filter(email=email).first()
        if existing_user:
            raise serializers.ValidationError('Ein Nutzer existiert bereits mit dieser Email.')

        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password']) #set pw with hashing algorithm
        user.save()
        return user
    
    #PATCH
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance
   