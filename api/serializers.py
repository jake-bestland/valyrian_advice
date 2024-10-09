from .models import CombinedData
from rest_framework import serializers

# class AdviceSlipSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdviceSlip
#         fields = 'advice'


class CombinedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CombinedData
        fields = ['advice', 'translation']