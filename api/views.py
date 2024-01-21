from rest_framework import generics
from django.http import HttpResponse
from speed_test.models import Fixed, Mobile, Historical
from .serializers import FixedSerializer, FixedCountrySerializer, FixedCountryAreaSerializer, FixedCountryAreaProviderSerializer, FixedCountryAreaPeriodSerializer, FixedCountryAreaPeriodDataSerializer
from .serializers import MobileCountrySerializer, MobileCountryAreaSerializer, MobileCountryAreaProviderSerializer, MobileCountryAreaPeriodSerializer, MobileCountryAreaPeriodDataSerializer
from .serializers import HistoricalCountrySerializer, HistoricalCountryAreaSerializer, HistoricalCountryAreaPeriodSerializer, HistoricalCountryAreaPeriodDataMobileSerializer, HistoricalCountryAreaPeriodDataFixedSerializer


def HomePageView(response):
    return HttpResponse("Hello, World!")


class FixedAPIView(generics.ListAPIView):
    queryset = Fixed.objects.all()[:10]
    serializer_class = FixedSerializer

class FixedCountryView(generics.ListAPIView):
    serializer_class = FixedCountrySerializer

    def get_queryset(self):
        queryset = Fixed.objects.all()
        countries = queryset.values('country').order_by('country').distinct()
        serializer = FixedCountrySerializer(countries, many=True)
        return serializer.data
        
class FixedCountryAreaView(generics.ListAPIView):
    serializer_class = FixedCountryAreaSerializer

    def get_queryset(self):
        queryset = Fixed.objects.all()
        country = self.request.query_params.get('country')
        #area = self.request.query_params.get('area')
        if country is not None:
            queryset = queryset.filter(country=country).order_by('area')
            areas = queryset.values('country', 'area').distinct()
            serializer = FixedCountryAreaSerializer(areas, many=True)
            return serializer.data
        else:
            queryset = Fixed.objects.none()
            return queryset
        
class FixedCountryAreaProviderView(generics.ListAPIView):
    serializer_class = FixedCountryAreaProviderSerializer

    def get_queryset(self):
        queryset = Fixed.objects.all()
        country = self.request.query_params.get('country')
        area = self.request.query_params.get('area')
        if country is not None and area is not None:
            queryset = queryset.filter(country=country, area=area).order_by('provider_name')
            provider_names = queryset.values('country', 'area', 'provider_name').distinct()
            serializer = FixedCountryAreaProviderSerializer(provider_names, many=True)
            return serializer.data
        else:
            queryset = Fixed.objects.none()
            return queryset
        
class FixedCountryAreaPeriodView(generics.ListAPIView):
    serializer_class = FixedCountryAreaPeriodSerializer

    def get_queryset(self):
        queryset = Fixed.objects.all()
        country = self.request.query_params.get('country')
        area = self.request.query_params.get('area')
        if country is not None and area is not None:
            queryset = queryset.filter(country=country, area=area).order_by('period')
            periods = queryset.values('country', 'area', 'period').distinct()
            #for i in range(len(periods)):
                #periods[i]['period'] = periods[i]['period'].strftime("%B %Y")
                #periods[i]['period'] = periods[i]['period'].strftime("%Y-%m-%d")
                
            serializer = FixedCountryAreaPeriodSerializer(periods, many=True)
            return serializer.data
        else:
            queryset = Fixed.objects.none()
            return queryset
        
class FixedCountryAreaPeriodDataView(generics.ListAPIView):
    serializer_class = FixedCountryAreaPeriodDataSerializer

    def get_queryset(self):
        queryset = Fixed.objects.all()
        country = self.request.query_params.get('country')
        area = self.request.query_params.get('area')
        period = self.request.query_params.get('period')
        if country is not None and area is not None and period is not None:
            print(period)
            queryset = queryset.filter(country=country, area=area, period=period)#.order_by('provider_name')
            speeds = queryset.values('country', 'area', 'period', 'provider_name', 'p25_download_mbps', 'p75_download_mbps').distinct()
            print(speeds)
            # for i in range(len(data)):
            #     data[i]['period'] = data[i]['period'].strftime("%Y-%m-%d")
                
            serializer = FixedCountryAreaPeriodDataSerializer(speeds, many=True)
            return serializer.data
        else:
            queryset = Fixed.objects.none()
            return queryset


class MobileCountryView(generics.ListAPIView):
    serializer_class = MobileCountrySerializer

    def get_queryset(self):
        queryset = Mobile.objects.all()
        countries = queryset.values('country').order_by('country').distinct()
        serializer = MobileCountrySerializer(countries, many=True)
        return serializer.data
        
class MobileCountryAreaView(generics.ListAPIView):
    serializer_class = MobileCountryAreaSerializer

    def get_queryset(self):
        queryset = Mobile.objects.all()
        country = self.request.query_params.get('country')
        #area = self.request.query_params.get('area')
        if country is not None:
            queryset = queryset.filter(country=country).order_by('area')
            areas = queryset.values('country', 'area').distinct()
            serializer = MobileCountryAreaSerializer(areas, many=True)
            return serializer.data
        else:
            queryset = Mobile.objects.none()
            return queryset
        
class MobileCountryAreaProviderView(generics.ListAPIView):
    serializer_class = MobileCountryAreaProviderSerializer

    def get_queryset(self):
        queryset = Mobile.objects.all()
        country = self.request.query_params.get('country')
        area = self.request.query_params.get('area')
        if country is not None and area is not None:
            queryset = queryset.filter(country=country, area=area).order_by('provider_name')
            provider_names = queryset.values('country', 'area', 'provider_name').distinct()
            serializer = MobileCountryAreaProviderSerializer(provider_names, many=True)
            return serializer.data
        else:
            queryset = Mobile.objects.none()
            return queryset
        
class MobileCountryAreaPeriodView(generics.ListAPIView):
    serializer_class = MobileCountryAreaPeriodSerializer

    def get_queryset(self):
        queryset = Mobile.objects.all()
        country = self.request.query_params.get('country')
        area = self.request.query_params.get('area')
        if country is not None and area is not None:
            queryset = queryset.filter(country=country, area=area).order_by('period')
            periods = queryset.values('country', 'area', 'period').distinct()
            #for i in range(len(periods)):
                #periods[i]['period'] = periods[i]['period'].strftime("%B %Y")
                #periods[i]['period'] = periods[i]['period'].strftime("%Y-%m-%d")
                
            serializer = MobileCountryAreaPeriodSerializer(periods, many=True)
            return serializer.data
        else:
            queryset = Mobile.objects.none()
            return queryset
        
class MobileCountryAreaPeriodDataView(generics.ListAPIView):
    serializer_class = MobileCountryAreaPeriodDataSerializer

    def get_queryset(self):
        queryset = Mobile.objects.all()
        country = self.request.query_params.get('country')
        area = self.request.query_params.get('area')
        period = self.request.query_params.get('period')
        if country is not None and area is not None and period is not None:
            print(period)
            queryset = queryset.filter(country=country, area=area, period=period)#.order_by('provider_name')
            speeds = queryset.values('country', 'area', 'period', 'provider_name', 'p25_download_mbps', 'p75_download_mbps').distinct()
            print(speeds)
            # for i in range(len(data)):
            #     data[i]['period'] = data[i]['period'].strftime("%Y-%m-%d")
                
            serializer = MobileCountryAreaPeriodDataSerializer(speeds, many=True)
            return serializer.data
        else:
            queryset = Mobile.objects.none()
            return queryset
        

class HistoricalCountryView(generics.ListAPIView):
    serializer_class = HistoricalCountrySerializer

    def get_queryset(self):
        queryset = Historical.objects.all()
        countries = queryset.values('country').order_by('country').distinct()
        serializer = HistoricalCountrySerializer(countries, many=True)
        return serializer.data
        
class HistoricalCountryAreaView(generics.ListAPIView):
    serializer_class = HistoricalCountryAreaSerializer

    def get_queryset(self):
        queryset = Historical.objects.all()
        country = self.request.query_params.get('country')
        #area = self.request.query_params.get('area')
        if country is not None:
            queryset = queryset.filter(country=country).order_by('area')
            areas = queryset.values('country', 'area').distinct()
            serializer = HistoricalCountryAreaSerializer(areas, many=True)
            return serializer.data
        else:
            queryset = Historical.objects.none()
            return queryset

class HistoricalCountryAreaPeriodView(generics.ListAPIView):
    serializer_class = HistoricalCountryAreaPeriodSerializer

    def get_queryset(self):
        queryset = Historical.objects.all()
        country = self.request.query_params.get('country')
        area = self.request.query_params.get('area')
        if country is not None and area is not None:
            queryset = queryset.filter(country=country, area=area).order_by('period')
            periods = queryset.values('country', 'area', 'period').distinct()
            #for i in range(len(periods)):
                #periods[i]['period'] = periods[i]['period'].strftime("%B %Y")
                #periods[i]['period'] = periods[i]['period'].strftime("%Y-%m-%d")
                
            serializer = HistoricalCountryAreaPeriodSerializer(periods, many=True)
            return serializer.data
        else:
            queryset = Historical.objects.none()
            return queryset
        
class HistoricalCountryAreaPeriodDataMobileView(generics.ListAPIView):
    serializer_class = HistoricalCountryAreaPeriodDataMobileSerializer

    def get_queryset(self):
        queryset = Historical.objects.all()
        country = self.request.query_params.get('country')
        area = self.request.query_params.get('area')
        period = self.request.query_params.get('period')
        if country is not None and area is not None and period is not None:
            print(period)
            queryset = queryset.filter(country=country, area=area, period=period)#.order_by('provider_name')
            speeds = queryset.values('country', 'area', 'period', 'mobile_median_download_mbps', 'mobile_median_upload_mbps', 'mobile_latency').distinct()
            print(speeds)
                
            serializer = HistoricalCountryAreaPeriodDataMobileSerializer(speeds, many=True)
            return serializer.data
        else:
            queryset = Historical.objects.none()
            return queryset
        
class HistoricalCountryAreaPeriodDataFixedView(generics.ListAPIView):
    serializer_class = HistoricalCountryAreaPeriodDataFixedSerializer

    def get_queryset(self):
        queryset = Historical.objects.all()
        country = self.request.query_params.get('country')
        area = self.request.query_params.get('area')
        period = self.request.query_params.get('period')
        if country is not None and area is not None and period is not None:
            print(period)
            queryset = queryset.filter(country=country, area=area, period=period)#.order_by('provider_name')
            speeds = queryset.values('country', 'area', 'period', 'fixed_median_download_mbps', 'fixed_median_upload_mbps', 'fixed_latency').distinct()
            print(speeds)
                
            serializer = HistoricalCountryAreaPeriodDataFixedSerializer(speeds, many=True)
            return serializer.data
        else:
            queryset = Historical.objects.none()
            return queryset