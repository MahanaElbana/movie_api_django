from .models import Movie
from rest_framework import serializers


## def name_len(value):
##         if len(value) < 2:
##             raise serializers.ValidationError("name is too short !")     
##          
## 
# first type (serializers.Serializer)
##class MovieSerializer(serializers.Serializer):
##    
##    id = serializers.IntegerField(read_only=True)
##    name = serializers.CharField(validators=[name_len])
##    description = serializers.CharField()
##    active = serializers.BooleanField()
##
##    def create(self, validated_data):
##        return Movie.objects.create(**validated_data)
##
##    def update(self, instance, validated_data):
##                                           # key  ,  value 
##        instance.name = validated_data.get('name', instance.name)
##        instance.description = validated_data.get('description', instance.description)
##        instance.active = validated_data.get('active', instance.active)
##        return instance    
##
##        #validate_<field_name>    
##    ##def validate_name(self ,value):
##    ##    """
##    ##    validate method 1 .
##    ##    """
##    ##    if len(value) < 2:
##    ##        raise serializers.ValidationError("name is too short !")     
##    ##    else:
##    ##        return value     
##
##    def validate(self, data): 
##        """
##        validate method 2.
##        """
##        if data['name'] == data['description']:
##            raise serializers.ValidationError("name should not equal description")
##        return data


class MovieSerializer(serializers.ModelSerializer):
    
    TRIPLEM_length = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = "__all__"
        #exclude = ['name']

    def get_TRIPLEM_length(self ,object):
        return len(object.name)    

    def validate(self, data): 
        """
        validate method 2.
        """
        if data['name'] == data['description']:
            raise serializers.ValidationError("name should not equal description")
        return data
    
    def validate_name(self ,value):
        """
        validate method 1 .
        """
        if len(value) < 2:
            raise serializers.ValidationError("name is too short !")     
        else:
            return value 