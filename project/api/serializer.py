
from .models import StreamPlatform ,Review ,WatchList
from rest_framework import serializers

from django.contrib.auth.models import  User
from django.contrib.auth.password_validation import validate_password 

class WatchListSerializer(serializers.ModelSerializer):
          class Meta :
              model = WatchList
              fields="__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):

  TRIPLEM_length = serializers.SerializerMethodField()
  def get_TRIPLEM_length(self ,object):
     return len(object.name)  

  '''   Serializer relations
           - Nested relationships
           - StringRelatedField
           - PrimaryKeyRelatedField
           - HyperlinkedRelatedField
 '''  

   

  watchList = WatchListSerializer(many=True, read_only=True) #Nested relationships
  #watchList = serializers.StringRelatedField(many=True, read_only=True)
  #watchList = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  #watchList = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name="movie_list_rest")

  class Meta :
       model = StreamPlatform
       fields="__all__"


class ReviewSerializer(serializers.ModelSerializer):
   user_review = serializers.StringRelatedField(read_only=True)
   watchlist = serializers.StringRelatedField(read_only=True)
   class Meta :
      model = Review
      #exclude =('watchlist',)
      fields ="__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True) #
    #password = serializers.CharField(write_only=True) 
    class Meta:
      model = User
      fields = ('username','first_name', 'last_name', 'email', 'password','password1', )
      extra_kwargs = {'password':{'write_only':True},}

    def validate(self, attr):
       print(attr)
       validate_password(attr['password'])
       print(validate_password(attr['password']))
       return attr

    def create(self,validated_data):
        if  validated_data['password'] != validated_data['password1'] :
           raise serializers.ValidationError("the same")

        if  User.objects.filter(email= validated_data['email']).exists() :
           raise serializers.ValidationError("the email")  

        user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],

                )
        user.set_password(validated_data['password'])
        user.save()

        return user











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


#class MovieSerializer(serializers.ModelSerializer):
#    
#    TRIPLEM_length = serializers.SerializerMethodField()
#    class Meta:
#        model = Movie
#        fields = "__all__"
#        #exclude = ['name']
#
#    def get_TRIPLEM_length(self ,object):
#        return len(object.name)    
#
#    def validate(self, data): 
#        """
#        validate method 2.
#        """
#        if data['name'] == data['description']:
#            raise serializers.ValidationError("name should not equal description")
#        return data
#    
#    def validate_name(self ,value):
#        """
#        validate method 1 .
#        """
#        if len(value) < 2:
#            raise serializers.ValidationError("name is too short !")     
#        else:
#            return value 