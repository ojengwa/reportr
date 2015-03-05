from apps.users.models import Staff
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = ('first_name', 'last_name', 'username', 'email', 'picture', 'url')
