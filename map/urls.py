# urls.py in the map app
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'shapefiles', views.ShapefileViewSet)
router.register(r'ville', views.VilleViewSet)
router.register(r'route', views.RouteViewSet)
router.register(r'electric_line', views.ElectricLineViewSet)
router.register(r'region_maroc', views.RegionMarocViewSet)
router.register(r'waterarea_dakhla', views.WaterareaDakhlaViewSet)
router.register(r'waterway_doa', views.WaterwayDoaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('save_pv_data/', views.ShapefileViewSet.as_view({'post': 'save_pv_data'}), name='save_pv_data'),
    path('save_el_data/', views.ShapefileViewSet.as_view({'post': 'save_el_data'}), name='save_el_data'),
]
