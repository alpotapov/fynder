from django.shortcuts import render
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from data.models import Venue
from data.serializers import VenueSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
@api_view(['GET', 'POST'])
def use_case_1(request):
    if request.method == 'GET':
        data = Venue.objects.filter(id__in=[202, 203]).all()
        serializer = VenueSerializer(instance=data, many=True)

        print data
        print serializer

        return JSONResponse(serializer.data)


@csrf_exempt
@api_view(['GET', 'POST'])
def use_case_2(request):
    if request.method == 'GET':
        data = Venue.objects.all()
        serializer = VenueSerializer(instance=data, many=True)

        print data
        print serializer

        return JSONResponse(serializer.data)



@csrf_exempt
@api_view(['GET', 'POST'])
def venues_search(request):
    if request.method == 'GET':
        data = Venue.objects.all()
        serializer = VenueSerializer(instance=data, many=True)

        print data
        print serializer

        return JSONResponse(serializer.data)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        people = {
            'male': data['people']['male'],
            'female': data['people']['female'],
            'child': data['people']['child'],
        }

        budget = data['budget']
        time = data['time']
        activities = data['activities']

        # TODO: make a call to search function

        data = Venue.objects.all()
        serializer = VenueSerializer(instance=data[:10], many=True)

        print data
        print serializer

        return JSONResponse(serializer.data)