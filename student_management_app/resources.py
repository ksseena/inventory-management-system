from import_export import resources
from .models import StoreItems, StoreItems2

class StoreResource1(resources.ModelResource):
    class Meta:
        model = StoreItems

class StoreResource2(resources.ModelResource):
    class Meta:
        model = StoreItems2