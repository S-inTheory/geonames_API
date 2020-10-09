from django.db.models import Model, CharField


class Geoname(Model):
    geonameid = CharField(max_length=80)
    name = CharField(max_length=200)
    asciiname = CharField(max_length=200)
    alternatenames = CharField(max_length=10000)
    latitude = CharField(max_length=80)
    longtitude = CharField(max_length=80)
    feature_class = CharField(max_length=1)
    feature_code = CharField(max_length=10)
    country_code = CharField(max_length=2)
    cc2 = CharField(max_length=200)
    admin1_code = CharField(max_length=20)
    admin2_code = CharField(max_length=80)
    admin3_code = CharField(max_length=20)
    admin4_code = CharField(max_length=20)
    population = CharField(max_length=80)
    elevation = CharField(max_length=80)
    dem = CharField(max_length=80)
    timezone = CharField(max_length=40)
    modification_date = CharField(max_length=80)
