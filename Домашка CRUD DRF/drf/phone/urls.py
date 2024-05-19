from django.urls import path, include
from rest_framework import routers
from . views import PhoneViewSet


router = routers.DefaultRouter()
router.register('phones', PhoneViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls'))
]