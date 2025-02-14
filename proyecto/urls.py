from rest_framework import routers
from .api import ProyectoViewSet

routers=routers.DefaultRouter()

routers.register('api/proyecto', ProyectoViewSet, 'proyecto')

urlpatterns=routers.urls