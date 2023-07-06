from rest_framework import serializers
from .models import *

class SuvSerializer(serializers.Serializer):
    brend = serializers.CharField(max_length=50)
    narx = serializers.IntegerField()
    litr = serializers.CharField()
    batafsil = serializers.CharField(max_length=50)


class MijozSeriazlizer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'
    def validate_qarz(self, qiymat):
        if qiymat > 500000:
            raise serializers.ValidationError('qarzingiz juda kop')
        return qiymat

class AdminSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class HaydovchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = '__all__'

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'