from rest_framework import viewsets
from apps.users.models import Staff
from serializers import UserSerializer



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = UserSerializer