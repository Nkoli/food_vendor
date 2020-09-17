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

    def get_frequency_of_occurence(self, instance):
        return instance.days_of_occurence.count()


class OrderPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderPayment
        fields = ['id', 'amount_due', 'amount_paid']


class OrderSerializer(serializers.ModelSerializer):
    order_payment = OrderPaymentSerializer(many=True)
    customer = serializers.ReadOnlyField(source='customer.name')

    class Meta:
        model = Order
        fields = ['id', 'customer', 'vendor', 'order_payment', 'status', 'menu', 'meal']

    def create(self, validated_data):
        meal = validated_data.pop('meal')
        payment_details = validated_data.pop('order_payment')
        order = Order.objects.create(**validated_data)
        for ml in meal:
            order.meal.add(ml)
        for payment_detail in payment_details:
            OrderPayment.objects.create(order=order, **payment_detail)
        return order

    def update(self, instance, validated_data):
        payment_details = validated_data.pop('order_payment')
        payments = (instance.order_payment).all()
        payments = list(payments)
        meal = validated_data.get('meal')
        if meal:
            instance.meal.add(*meal)
        instance.vendor = validated_data.get('vendor', instance.vendor)
        instance.status = validated_data.get('status', instance.status)
        instance.menu = validated_data.get('menu', instance.menu)
        instance.save()

        for payment_detail in payment_details:
            payment = payments.pop(0)
            payment.amount_due = payment_detail.get('amount_due', payment.amount_due)
            payment.amount_paid = payment_detail.get('amount_paid', payment.amount_paid)
            payment.save()

        return instance


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

    def get_frequency_of_occurence(self, instance):
        return instance.days_of_occurence.count()


class OrderPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderPayment
        fields = ['id', 'amount_due', 'amount_paid']


class OrderSerializer(serializers.ModelSerializer):
    order_payment = OrderPaymentSerializer(many=True)
    customer = serializers.ReadOnlyField(source='customer.name')

    class Meta:
        model = Order
        fields = ['id', 'customer', 'vendor', 'order_payment', 'status', 'menu', 'meal']

    def create(self, validated_data):
        meal = validated_data.pop('meal')
        payment_details = validated_data.pop('order_payment')
        order = Order.objects.create(**validated_data)
        for ml in meal:
            order.meal.add(ml)
        for payment_detail in payment_details:
            OrderPayment.objects.create(order=order, **payment_detail)
        return order

    def update(self, instance, validated_data):
        payment_details = validated_data.pop('order_payment')
        payments = (instance.order_payment).all()
        payments = list(payments)
        meal = validated_data.get('meal')
        if meal:
            instance.meal.add(*meal)
        instance.vendor = validated_data.get('vendor', instance.vendor)
        instance.status = validated_data.get('status', instance.status)
        instance.menu = validated_data.get('menu', instance.menu)
        instance.save()

        for payment_detail in payment_details:
            payment = payments.pop(0)
            payment.amount_due = payment_detail.get('amount_due', payment.amount_due)
            payment.amount_paid = payment_detail.get('amount_paid', payment.amount_paid)
            payment.save()

        return instance
