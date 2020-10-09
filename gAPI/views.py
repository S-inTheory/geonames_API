import json
import os

import pendulum
from django.db.models import Max, Min
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from gAPI.models import Geoname
from gAPI.serializers import GeonameSerializer
from geonames_API.settings import BASE_DIR


def get_data():
    json_data = os.path.join(BASE_DIR, 'static', '../static/geonames.json')
    response = open(json_data)
    if not response:
        return
    data_json = json.load(response)
    return data_json


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class GeonamesListView(ListAPIView):
    queryset = Geoname.objects.all()
    serializer_class = GeonameSerializer
    pagination_class = StandardResultsSetPagination


class GeonamesDetailView(APIView):
    def get(self, request, id):
        geoname = get_object_or_404(Geoname, geonameid=id)
        serializer = GeonameSerializer(geoname)
        return Response(serializer.data)


class GeonamesSearchView(APIView):
    def get(self, request, search):

        # Gaining information about two cities from request

        city_1 = search.split(',')[0]
        city_2 = search.split(',')[1]

        query_1 = Geoname.objects.filter(alternatenames__icontains=city_1)
        query_2 = Geoname.objects.filter(alternatenames__icontains=city_2)

        # Gaining information about population in city 1

        query_1_max_population = query_1.aggregate(Max('population'))['population__max']
        query_1_min_population = query_1.aggregate(Min('population'))['population__min']

        # and city 2

        query_2_max_population = query_2.aggregate(Max('population'))['population__max']
        query_2_min_population = query_2.aggregate(Min('population'))['population__min']

        # Checking the quantity of cities(objects in queryset)
        # and doing needed operations to have only two cities

        if len(query_1) > 1:
            query_1 = Geoname.objects.filter(alternatenames__icontains=city_1, population=query_1_max_population)
            if query_1_max_population == query_1_min_population:
                query_1 = Geoname.objects.filter(alternatenames__icontains=city_1, geonameid=query_1[0].geonameid)
        if len(query_2) > 1:
            query_2 = Geoname.objects.filter(alternatenames__icontains=city_2, population=query_2_max_population)
            if query_2_max_population == query_2_min_population:
                query_2 = Geoname.objects.filter(alternatenames__icontains=city_2, geonameid=query_2[0].geonameid)

        # Queryset with two cities

        cities = query_1 | query_2

        # Checking max latitude for northern city and gaining northern city

        max_latitude = cities.values_list('latitude', flat=True).aggregate(Max('latitude'))['latitude__max']
        northern_city = cities.filter(latitude=max_latitude).values('name')[0]['name']

        # Collecting queryset in list for better manipulating

        result = []
        for data in cities.values():
            result.append(data)

        # Operation for gaining timezone difference in given cities

        timezone_comparison = result[0]['timezone'] == result[1]['timezone']
        city_1_timezone = result[0]['timezone']
        time_city_1 = pendulum.datetime(2000, 1, 1, tz=city_1_timezone)
        city_2_timezone = pendulum.timezone(result[1]['timezone'])
        time_city_2 = pendulum.datetime(2000, 1, 1, tz=city_2_timezone)
        time_difference = time_city_1.diff(time_city_2).in_hours()

        # Data for additional information about two cities

        comparison = {'northern_city': northern_city,
                      'equal_timezones': timezone_comparison,
                      'timezone_difference_in_hours': time_difference}
        result.append(comparison)

        return Response(result)
