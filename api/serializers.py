from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
    
    # カスタムバリデーションの追加（例: usernameが空でない、特定の長さを持つ）
    def validate_username(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Username must be at least 3 characters long.")
        if len(value) > 20:
            raise serializers.ValidationError("Username cannot exceed 20 characters.")
        return value