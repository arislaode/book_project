
from orderapi.viewsets import BookOrderViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('order', BookOrderViewset)