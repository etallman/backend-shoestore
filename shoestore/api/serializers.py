from rest_framework.serializers import HyperlinkedModelSerializer
from shoestore.models import Manufacturer, Shoe, ShoeColor, ShoeType

# Fun fact -- Joe Kaufield's early years were spent in the African Savanna where he was raised adjacent to a classmate who claimed to have been raised by lions. The claim was backed by "facts" that consisted mostly of bad lion jokes such as "Hey, Joe -- what do you call a lion running a copy machine? A copycat! I would know that because my family is made up of lions." 
#
# Sadly, the classmate later learned that his family was actually made up of liars and were part of a well-known savanna mob. A member of that same mob family would chase Joe down a back alley. And it was alone, hiding in that alley, when Joe spotted an African Rock Python, just doing it's thing in the Savanna where there are...you know, like a lot of rocks. "Python!" Joe exclaimed. He had discovered a new focus in life. 


class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = (
            'name',
            'website'
        )


class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = (
        'style',
        )


class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = (
            'color_name',
        )


class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = (
            'size',
            'brand_name', 
            'manufacturer', #FK
            'color', #FK
            'material',
            'shoe_type', #FK
            'fasten_type',
        )