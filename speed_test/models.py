from django.db import models

class Fixed(models.Model):

    country = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    service = models.CharField(max_length=6)
    provider_name = models.CharField(max_length=100)
    provider_id = models.IntegerField()
    period = models.CharField(max_length=7)
    p25_download_mbps = models.DecimalField(max_digits=7, decimal_places=2)
    p75_download_mbps = models.DecimalField(max_digits=7, decimal_places=2)

class Mobile(models.Model):

    country = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    service = models.CharField(max_length=6)
    provider_name = models.CharField(max_length=100)
    provider_id = models.IntegerField()
    period = models.CharField(max_length=7)
    p25_download_mbps = models.DecimalField(max_digits=7, decimal_places=2)
    p75_download_mbps = models.DecimalField(max_digits=7, decimal_places=2)

class Historical(models.Model):

    country = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    period = models.CharField(max_length=7)
    mobile_median_download_mbps = models.DecimalField(max_digits=7, decimal_places=2)
    mobile_median_upload_mbps = models.DecimalField(max_digits=7, decimal_places=2)
    mobile_latency = models.IntegerField()
    fixed_median_download_mbps = models.DecimalField(max_digits=7, decimal_places=2)
    fixed_median_upload_mbps = models.DecimalField(max_digits=7, decimal_places=2)
    fixed_latency = models.IntegerField()