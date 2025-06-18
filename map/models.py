# models.py in the map app
from django.contrib.gis.db import models

class Shapefile(models.Model):
    gid = models.AutoField(primary_key=True)
    join_count = models.IntegerField()
    target_fid = models.IntegerField()
    id = models.IntegerField()
    mois1 = models.FloatField()
    mois2 = models.FloatField()
    mois3 = models.FloatField()
    mois4 = models.FloatField()
    mois5 = models.FloatField()
    mois6 = models.FloatField()
    mois7 = models.FloatField()
    mois8 = models.FloatField()
    mois9 = models.FloatField()
    mois10 = models.FloatField()
    mois11 = models.FloatField()
    mois12 = models.FloatField()
    ghi = models.FloatField()
    dhi = models.FloatField()
    bni = models.FloatField()
    temp_avg = models.FloatField()
    srtm = models.FloatField()
    ws_10m = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.GeometryField()

    class Meta:
         db_table = 'shapefiles'

    def __str__(self):
        return self.id




class PV(models.Model):
    gid = models.AutoField(primary_key=True)
    ghi = models.FloatField()
    area = models.FloatField()
    geom = models.GeometryField()
    exp_pv = models.BooleanField()
    f_e = models.FloatField()
    pv = models.FloatField()
    p_pv = models.FloatField()

    class Meta:
        db_table = 'pv'

    def __str__(self):
        return str(self.id)
    

class El(models.Model):
    gid = models.AutoField(primary_key=True)
    w_s = models.FloatField()
    area = models.FloatField()
    geom = models.GeometryField()
    exp_el = models.BooleanField()
    f_e = models.FloatField()
    el = models.FloatField()
    p_el = models.FloatField()

    class Meta:
        db_table = 'el'

    def __str__(self):
        return str(self.id)
    

class ville(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    geom = models.GeometryField()

    class Meta:
        db_table = 'ville'

    def __str__(self):
        return self.name
class route(models.Model):
    gid = models.AutoField(primary_key=True)
    geom = models.GeometryField()

    class Meta:
        db_table = 'route'

    def __str__(self):
        return str(self.id)

class electric_line(models.Model):
    gid = models.AutoField(primary_key=True)
    geom = models.GeometryField()

    class Meta:
        db_table = 'electric_line'

    def __str__(self):
        return str(self.id)

class region_maroc(models.Model):
    gid = models.AutoField(primary_key=True)
    geom = models.GeometryField()

    class Meta:
        db_table = 'region_maroc'

    def __str__(self):
        return str(self.id)
class waterarea_dakhla(models.Model):
    gid = models.AutoField(primary_key=True)
    geom = models.GeometryField()

    class Meta:
        db_table = 'waterarea_dakhla'

    def __str__(self):
        return str(self.id)

class waterway_doa(models.Model):
    gid = models.AutoField(primary_key=True)
    geom = models.GeometryField()

    class Meta:
        db_table = 'waterway_doa'

    def __str__(self):
        return str(self.id)