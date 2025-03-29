from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'followers_count']
        extra_kwargs = {
            'followers': {'read_only': True},
        }
    
    def get_followers_count(self, obj):
        return obj.followers.count()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        min_length=8,
        error_messages={
            'min_length': _('Password must be at least 8 characters long.')
        }
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        label=_('Confirm Password')
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'email': {'required': True}
        }
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password2': _('The two password fields must match.')}
            )
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)
        return user