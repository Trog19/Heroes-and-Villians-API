from rest_framework.decorators import api_view
from rest_framework.response import Response

from supers import serializers
from .models import Super
from .serializers import SuperSerializer

@api_view(['GET'])
def supers_list(request):

    super = Super.objects.all()

    serializers = SuperSerializer(super, many=True)


    return Response (serializers.data)