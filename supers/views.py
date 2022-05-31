from django.urls import set_urlconf
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from supers import serializers
from .models import Super
from .serializers import SuperSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        super = Super.objects.all()
        serializers = SuperSerializer(super, many=True)
        return Response (serializers.data)
    elif request.method == 'POST':
        serializers = SuperSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializers = SuperSerializer(super)
        return Response(serializers.data)
    elif request.method == 'PUT':
        serializers = SuperSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def supers_detail(request):
    hero_param = request.query_params.filter(super_type_id = 1)
    villain_param = request.query_params.filter(super_type_id = 2)
    if request.method == 'GET':
        if hero_param:
            # super = Super.objects.filter(super_type_id = 1)
            serializers = SuperSerializer(hero_param, many=True)
            return Response (serializers.data)
        elif villain_param:
            # super = Super.objects.filter(super_type_id = 2)
            serializers = SuperSerializer(villain_param, many=True)
            return Response(serializers.data)




        # super = Super.objects.filter(super_type_id = 2)
    #     serializers = SuperSerializer(super, many=True)
    #     return Response (serializers.data)
