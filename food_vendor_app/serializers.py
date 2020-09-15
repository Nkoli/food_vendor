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
    vendor = serializers.ReadOnlyField(source='vendor.name')
    frequency_of_occurence = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'name', 'meals', 'vendor', 'dietary_type',
                  'description', 'days_of_occurence', 'frequency_of_occurence']

    def update(self, instance, validated_data):
        meals = validated_data.get('meals')
        if meals:
            instance.meals.add(*meals)

        days_of_occurence = validated_data.get('days_of_occurence')
        if days_of_occurence:
            instance.days_of_occurence.add(*days_of_occurence)

        instance.name = validated_data.get('name', instance.name)
        instance.dietary_type = validated_data.get('dietary_type', instance.dietary_type)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    def get_frequency_of_occurence(self, obj):
        return obj.days_of_occurence.count()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPayment
        fields = '__all__'
