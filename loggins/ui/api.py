from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL

from ui.models import Record


class RecordResource(ModelResource):
    class Meta:
        queryset = Record.objects.all()
        resource_name = 'record'
        authentication = BasicAuthentication()
        authorization = Authorization()
        filtering = {
                'hostname': ALL,
                'event': ALL,
                'timestamp': ALL,
            }
