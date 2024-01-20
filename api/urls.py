from django.urls import path
from .views import FixedAPIView, FixedCountryView, FixedCountryAreaView, FixedCountryAreaProviderView, FixedCountryAreaPeriodView, FixedCountryAreaPeriodDataView
from .views import MobileCountryView, MobileCountryAreaView, MobileCountryAreaProviderView, MobileCountryAreaPeriodView, MobileCountryAreaPeriodDataView
from .views import HistoricalCountryView, HistoricalCountryAreaView, HistoricalCountryAreaPeriodView, HistoricalCountryAreaPeriodDataMobileView, HistoricalCountryAreaPeriodDataFixedView

urlpatterns = [
    path("", FixedAPIView.as_view()),
    path("fixed/countries/", FixedCountryView.as_view()),
    path("fixed/areas_per_country/", FixedCountryAreaView.as_view()),
    path("fixed/providers_per_area/", FixedCountryAreaProviderView.as_view()),
    path("fixed/periods_per_area/", FixedCountryAreaPeriodView.as_view()),
    path("fixed/speeds/", FixedCountryAreaPeriodDataView.as_view()),
    path("mobile/countries/", MobileCountryView.as_view()),
    path("mobile/areas_per_country/", MobileCountryAreaView.as_view()),
    path("mobile/providers_per_area/", MobileCountryAreaProviderView.as_view()),
    path("mobile/periods_per_area/", MobileCountryAreaPeriodView.as_view()),
    path("mobile/speeds/", MobileCountryAreaPeriodDataView.as_view()),
    path("historical/countries/", HistoricalCountryView.as_view()),
    path("historical/areas_per_country/", HistoricalCountryAreaView.as_view()),
    path("historical/periods_per_area/", HistoricalCountryAreaPeriodView.as_view()),
    path("historical/mobile_speeds/", HistoricalCountryAreaPeriodDataMobileView.as_view()),
    path("historical/fixed_speeds/", HistoricalCountryAreaPeriodDataFixedView.as_view()),
]