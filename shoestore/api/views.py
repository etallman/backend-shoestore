from shoestore.models import Manufacturer, ShoeType, ShoeColor, Shoe
from shoestore.api.serializers import ManufacturerSerializer, ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


class ManufacturerViewSet(ModelViewSet):
    queryset=Manufacturer.objects.all()
    serializer_class='ManufacturerSerializer'
    basename='manufacturer'


class ShoeTypeViewSet(ModelViewSet):
    queryset=ShoeType.objects.all()
    serializer_class='ShoeTypeSerializer'
    basename='shoetype' 
    
    """
    localhost:8000/api/newsitem/ gets all items
    localhost:8000/api/newsitem/?id=5 ==> gets only 1 item
    """
    def get_queryset(self):
        queryset = ShoeType.objects.all()
        id_value = self.request.query_params.get('id', None)
        if id_value:
            queryset.filter(id=id_value)
        return queryset


class ShoeColorViewSet(ModelViewSet):
    queryset=ShoeType.objects.all()
    serializer_class='ShoeColorSerializer'
    basename='shoecolor'
    
    def get_queryset(self):
        queryset = ShoeType.objects.all()
        id_value = self.request.query_params.get('id', None)
        if id_value:
            queryset.filter(id=id_value)
        return queryset


class ShoeViewSet(ModelViewSet):
    queryset=Shoe.objects.all()
    serializer_class='ShoeSerializer'
    basename='shoe'
    
    
    # @action(detail = False, methods=['GET', 'POST'])
    # def hello(self, request):       
    # 