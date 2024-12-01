from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from django_filters import rest_framework as filters
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse
import json
from rest_framework import viewsets
from rest_framework.decorators import action,api_view
# list, retrieve, create, delete
from json import dumps
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import requests


# ADD YOUR API KEY HERE:

# This is the DeepL API Url as of 15/11/2024
DEEPL_API_URL = 'https://api-free.deepl.com/v2/translate'
js = {}

with open('key_username_password.json', 'r') as f:
    js = json.load(f)

DEEPL_API_KEY = js['deepl_key'] 
PROXY_KEY = js['proxy_key']


@csrf_exempt
@api_view(['POST'])
def makeProxy(request):

    print(request.data)
    data = (request.data)

    print(request.POST)

    if not (data.get('key')):
        response = { "error": "Bad proxy key" }
        return JsonResponse(response.json(), status=400)

    if not (data['key'] == PROXY_KEY):
        response = { "error": "Bad proxy key" }
        return JsonResponse(response.json(), status=400)

    print(f'text received: {data["text"]}')

    deepl_payload = {
        'auth_key': DEEPL_API_KEY,
        'text': data['text'],
        'target_lang': data['target_lang'],
        'source_lang':data['source_lang']
    }

    response = requests.post(DEEPL_API_URL, data=deepl_payload)
    print(response.json())

    if response.status_code == 200:
        return JsonResponse(response.json(), status=200)
    else:
        return JsonResponse({
            'error': 'Failed to communicate with DeepL',
            'details': response.text
        }, status=response.status_code)
