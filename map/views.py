from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry
from .models import Shapefile, PV, El, ville, route, electric_line, region_maroc, waterarea_dakhla, waterway_doa
from django.db.models import Avg
from .serializers import ShapefileSerializer, PvSerializer, ElSerializer, VilleSerializer, RouteSerializer, ElectricLineSerializer, RegionMarocSerializer, WaterareaDakhlaSerializer, WaterwayDoaSerializer
import json

class ShapefileViewSet(viewsets.ModelViewSet):
    queryset = Shapefile.objects.all()
    serializer_class = ShapefileSerializer

    @action(detail=False, methods=['post'])
    def intersect(self, request):
        geom = request.data.get('geometry')
        if geom:
            try:
                geojson_geom = json.dumps(geom)
                geom = GEOSGeometry(geojson_geom)
            except Exception as e:
                return Response({"error": "Invalid geometry provided"}, status=400)
            
            queryset = Shapefile.objects.filter(geom__intersects=geom)

            # Check if the geometry is a Point (1), LineString (2), or Polygon (3)
            geom_type = geom.geom_type

            if geom_type == 'Point':
                averages = queryset.aggregate(
                    avg_mois1=Avg('mois1'),
                    avg_mois2=Avg('mois2'),
                    avg_mois3=Avg('mois3'),
                    avg_mois4=Avg('mois4'),
                    avg_mois5=Avg('mois5'),
                    avg_mois6=Avg('mois6'),
                    avg_mois7=Avg('mois7'),
                    avg_mois8=Avg('mois8'),
                    avg_mois9=Avg('mois9'),
                    avg_mois10=Avg('mois10'),
                    avg_mois11=Avg('mois11'),
                    avg_mois12=Avg('mois12'),
                    avg_ghi=Avg('ghi'),
                    avg_dhi=Avg('dhi'),
                    avg_bni=Avg('bni'),
                    avg_temp_avg=Avg('temp_avg'),
                    avg_srtm=Avg('srtm'),
                    avg_ws_10m=Avg('ws_10m'),
                    avg_shape_area=Avg('shape_area')
                )
            else:
                averages = queryset.aggregate(
                    avg_mois1=Avg('mois1'),
                    avg_mois2=Avg('mois2'),
                    avg_mois3=Avg('mois3'),
                    avg_mois4=Avg('mois4'),
                    avg_mois5=Avg('mois5'),
                    avg_mois6=Avg('mois6'),
                    avg_mois7=Avg('mois7'),
                    avg_mois8=Avg('mois8'),
                    avg_mois9=Avg('mois9'),
                    avg_mois10=Avg('mois10'),
                    avg_mois11=Avg('mois11'),
                    avg_mois12=Avg('mois12'),
                    avg_ghi=Avg('ghi'),
                    avg_dhi=Avg('dhi'),
                    avg_bni=Avg('bni'),
                    avg_temp_avg=Avg('temp_avg'),
                    avg_srtm=Avg('srtm'),
                    avg_ws_10m=Avg('ws_10m')
                    # Exclude shape_area
                )
                
            # Serialize the queryset and add averages to the response
            serializer = self.get_serializer(queryset, many=True)
            response_data = {
                "averages": averages,
                "features": serializer.data,
            }
            return Response(response_data)
        
        return Response({"error": "No geometry provided"}, status=400)


    @action(detail=False, methods=['post'])
    def save_pv_data(self, request):
        data = request.data
        print("Received data:", data)  # Log received data

        geom = data.get('geom')  # Corrected key to match received data

        if not geom:
            print("No geometry provided")
            return Response({"error": "No geometry provided"}, status=400)

        try:
            geojson_geom = json.dumps(geom)
            print("GeoJSON geometry:", geojson_geom)  # Log GeoJSON
            geom = GEOSGeometry(geojson_geom)
            print("Converted GEOSGeometry:", geom)  # Log converted geometry
        except Exception as e:
            print("Error parsing geometry:", e)
            return Response({"error": "Invalid geometry provided"}, status=400)

        serializer = PvSerializer(data={
            'ghi': data.get('ghi', 0),
            'area': data.get('area', 0),
            'geom': geom,
            'exp_pv': data.get('exp_pv', False),
            'f_e': data.get('f_e', 0),
            'pv': data.get('pv', 0),
            'p_pv': data.get('p_pv', 0),
        })
        
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "PV data saved successfully"})
        else:
            print("Validation errors:", serializer.errors)
            return Response({"error": "Data validation failed", "details": serializer.errors}, status=400)

    @action(detail=False, methods=['post'])
    def save_el_data(self, request):
        data = request.data
        print("Received data:", data)  # Log received data

        geom = data.get('geom')  # Corrected key to match received data

        if not geom:
            print("No geometry provided")
            return Response({"error": "No geometry provided"}, status=400)

        try:
            geojson_geom = json.dumps(geom)
            print("GeoJSON geometry:", geojson_geom)  # Log GeoJSON
            geom = GEOSGeometry(geojson_geom)
            print("Converted GEOSGeometry:", geom)  # Log converted geometry
        except Exception as e:
            print("Error parsing geometry:", e)
            return Response({"error": "Invalid geometry provided"}, status=400)

        serializer = ElSerializer(data={
            'w_s': data.get('w_s', 0),
            'area': data.get('area', 0),
            'geom': geom,
            'exp_el': data.get('exp_el', False),
            'f_e': data.get('f_e', 0),
            'el': data.get('el', 0),
            'p_el': data.get('p_el', 0),
        })
        
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "EL data saved successfully"})
        else:
            print("Validation errors:", serializer.errors)
            return Response({"error": "Data validation failed", "details": serializer.errors}, status=400)

class VilleViewSet(viewsets.ModelViewSet):
    queryset = ville.objects.all()
    serializer_class = VilleSerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = route.objects.all()
    serializer_class = RouteSerializer

class ElectricLineViewSet(viewsets.ModelViewSet):
    queryset = electric_line.objects.all()
    serializer_class = ElectricLineSerializer

class RegionMarocViewSet(viewsets.ModelViewSet):
    queryset = region_maroc.objects.all()
    serializer_class = RegionMarocSerializer

class WaterareaDakhlaViewSet(viewsets.ModelViewSet):
    queryset = waterarea_dakhla.objects.all()
    serializer_class = WaterareaDakhlaSerializer

class WaterwayDoaViewSet(viewsets.ModelViewSet):
    queryset = waterway_doa.objects.all()
    serializer_class = WaterwayDoaSerializer