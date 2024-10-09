# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import viewsets
from .models import CombinedData
from .serializers import CombinedDataSerializer
import requests

# Create your views here.
# @api_view(['GET'])
# def get_advice(request):
#     return Response(AdviceSlipSerializer({}))  # 


class CombinedDataViewSet(viewsets.ViewSet):
    # queryset = CombinedData
    # serializer_class = CombinedDataSerializer
    
    
    def list(self, request):
        advice_response = requests.get('https://api.adviceslip.com/advice')
        advice_slip = advice_response.json()
        advice = advice_slip['slip']['advice']

        translation_response = requests.post(
            'https://api.funtranslations.com/translate/valyrian.json',
            data={'text': advice, 'translation': 'valyrian'},
        )
        translation_data = translation_response.json()
        translation = translation_data['contents']['translated']

        combined_data = {
            'advice': advice,
            'translation': translation
        }
        serializer = CombinedDataSerializer(combined_data)
        return Response(serializer.data)