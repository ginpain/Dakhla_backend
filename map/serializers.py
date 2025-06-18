from rest_framework import serializers
from .models import Shapefile, PV, El, ville, route, electric_line, region_maroc, waterarea_dakhla, waterway_doa

class ShapefileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shapefile
        fields = '__all__'
        geo_field = 'geom'

class PvSerializer(serializers.ModelSerializer):
    class Meta:
        model = PV
        fields = '__all__'
        geo_field = 'geom'

class ElSerializer(serializers.ModelSerializer):
    class Meta:
        model = El
        fields = '__all__'
        geo_field = 'geom'

class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ville
        fields = '__all__'
        geo_field = 'geom'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = route
        fields = '__all__'
        geo_field = 'geom'

class ElectricLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = electric_line
        fields = '__all__'
        geo_field = 'geom'

class RegionMarocSerializer(serializers.ModelSerializer):
    class Meta:
        model = region_maroc
        fields = '__all__'
        geo_field = 'geom'

class WaterareaDakhlaSerializer(serializers.ModelSerializer):
    class Meta:
        model = waterarea_dakhla
        fields = '__all__'
        geo_field = 'geom'

class WaterwayDoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = waterway_doa
        fields = '__all__'
        geo_field = 'geom'
