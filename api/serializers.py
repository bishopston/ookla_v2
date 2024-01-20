from rest_framework import serializers
from speed_test.models import Fixed, Mobile, Historical

class FixedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixed
        fields = ('country', 'area', 'service', 'provider_name', 'provider_id', 'period', 'p25_download_mbps', 'p75_download_mbps')

    def to_representation(self, instance):
        representation = super(FixedSerializer, self).to_representation(instance)
        representation['period'] = (instance.period.strftime("%B") + ' ' + instance.period.strftime("%Y"))
        return representation
    
class FixedCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixed
        fields = ('country',)

class FixedCountryAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixed
        fields = ('country', 'area')

class FixedCountryAreaProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixed
        fields = ('country', 'area', 'provider_name')

class FixedCountryAreaPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixed
        fields = ('country', 'area', 'period')

class FixedCountryAreaPeriodDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixed
        fields = ('country', 'area', 'period', 'provider_name', 'p25_download_mbps', 'p75_download_mbps')


class MobileCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ('country',)

class MobileCountryAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ('country', 'area')

class MobileCountryAreaProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ('country', 'area', 'provider_name')

class MobileCountryAreaPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ('country', 'area', 'period')

class MobileCountryAreaPeriodDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ('country', 'area', 'period', 'provider_name', 'p25_download_mbps', 'p75_download_mbps')


class HistoricalCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Historical
        fields = ('country',)

class HistoricalCountryAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historical
        fields = ('country', 'area')

class HistoricalCountryAreaPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historical
        fields = ('country', 'area', 'period')

class HistoricalCountryAreaPeriodDataMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historical
        fields = ('country', 'area', 'period', 'mobile_median_download_mbps', 'mobile_median_upload_mbps', 'mobile_latency')

class HistoricalCountryAreaPeriodDataFixedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historical
        fields = ('country', 'area', 'period', 'fixed_median_download_mbps', 'fixed_median_upload_mbps', 'fixed_latency')