
from django.urls import path,include
from api.views import OltViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'olts', OltViewset)

urlpatterns = [
    path('',include(router.urls))
]