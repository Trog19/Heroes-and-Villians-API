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
        type_param = request.query_params.get('type')
        if type_param:
            supers_by_type = Super.objects.filter(super_type__super_type=type_param)
            serializer = SuperSerializer(supers_by_type, many=True)
            return Response(serializer.data)
        super = Super.objects.all()
        serializers = SuperSerializer(super, many=True)
        return Response (serializers.data)
    elif request.method == 'POST':
        serializers = SuperSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
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
def supers_type(request):
    type_param = request.query_params.get('type')
    if request.method == 'GET':
        if type_param:
            supers = Super.objects.filter(super_type__super_type=type_param)
            serializers = SuperSerializer(supers, many=True)
            return Response (serializers.data)
