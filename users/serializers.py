from rest_framework import serializers
from .models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'full_name', 'date_joined']
        read_only_fields = ['id', 'date_joined']
    
    def validate_email(self, value):
        """
        Validate email uniqueness and format
        """
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Enter a valid email address.")
        
        # Check if email already exists (excluding current instance during update)
        if self.instance and self.instance.email == value:
            return value
            
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        
        return value
    
    def validate_username(self, value):
        """
        Validate username uniqueness
        """
        if self.instance and self.instance.username == value:
            return value
            
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        
        return value