import django_filters.rest_framework
from . models import Phone
from . serializers import PhoneSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from . permissions import AllForAdminOtherReadOnly
from rest_framework import filters


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializers
    permission_classes = (AllForAdminOtherReadOnly, )
    filter_backends = [filters.OrderingFilter]
    search_fields = ['brand', 'mark', 'year', 'price_usd']