from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()

        return user

    def update(self, instance, validated_data):
        if self.is_valid(raise_exception=True):
            pass


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email',)
        # fields = '__all__'
        # exclude = ('password',)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        if self.is_valid(raise_exception=True):
            return instance
