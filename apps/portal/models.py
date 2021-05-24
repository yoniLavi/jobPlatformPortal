from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import JSONField
from django_extensions.db.models import models,  TimeStampedModel


class JobOffer(TimeStampedModel):
    title = models.CharField(max_length=500)
    company = models.CharField(max_length=500)
    platform = models.CharField(max_length=250)
    platform_id = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    url = models.CharField(max_length=500)
    application_url = models.CharField(max_length=500)
    raw_json = JSONField(encoder=DjangoJSONEncoder)
