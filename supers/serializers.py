from tarfile import SUPPORTED_TYPES
from rest_framework import serializers

from super_types import models
from . models import Super
from super_types.models import SuperType

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'super_type', 'super_type_id']
        super_type = models.SuperType(write_only=True)
        super_type_id = serializers.IntegerField(write_only=True)
