
from rest_framework import viewsets
from . import models
from . import serializers
# from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class BookOrderViewset(viewsets.ModelViewSet):
    queryset = models.BookOrder.objects.all()
    serializer_class = serializers.BookOrderSerializer
    # authentication_classes = (TokenAuthentication,)
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)