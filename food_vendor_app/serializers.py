from rest_framework import serializers

from .models import Meal, Menu, Order, OrderPayment, User


class UserRegisterSerializer(serializers.ModelSerializer):

    def validate(self, data):
        is_vendor = data.get('is_vendor')

        if is_vendor and not data.get('business_name'):
            raise serializers.ValidationError('Business name is required')
        return data

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone_number', 'password', 'is_vendor', 'business_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=200, required=True)
    password = serializers.CharField(required=True, write_only=True)


class MealSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.name')

    class Meta:
        model = Meal
        fields = ['id', 'name', 'vendor', 'description', 'metadata']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.metadata = validated_data.get('metadata', instance.metadata)
        instance.save()
        return instance


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPayment
        fields = '__all__'
