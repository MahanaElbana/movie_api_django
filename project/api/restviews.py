
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import Review ,StreamPlatform ,WatchList 
from .serializer import WatchListSerializer ,StreamPlatformSerializer ,ReviewSerializer ,RegisterSerializer
from rest_framework import viewsets ,generics 
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from .permission import IsAdminUserOrReadOnly, ReviewReadOnly
from rest_framework.authtoken.models import Token
#! stream/movie_id/review
#class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#    queryset = Review.objects.all()
#    serializer_class = ReviewSerializer
#
#    def get(self, request, *args, **kwargs):
#        return self.list(request, *args, **kwargs)
#
#    def post(self, request, *args, **kwargs):
#        return self.create(request, *args, **kwargs)

class ReviewList(generics.ListAPIView):
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        print(self.kwargs)
        #print(self.request)
        pk = self.kwargs['pk']
        movie = WatchList.objects.get(pk=pk)
        #return Review.objects.filter(watchlist=pk)
        return Review.objects.filter(watchlist=movie)
         
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
       pk = self.kwargs['pk']
       movie = WatchList.objects.get(pk=pk)
       print(movie)
       user =self.request.user            #watchlist = movie
       review_user =Review.objects.filter(watchlist = pk ,user_review =user)
       if review_user.exists() :
           raise ValidationError("hello pro !")
       #create review with watchlist passed
       print(serializer.validated_data)
       if movie.avarage_rating == 0.0:
           movie.avarage_rating = serializer.validated_data['rating']
       else :
           movie.avarage_rating = (movie.avarage_rating + serializer.validated_data['rating'])/2
       movie.number_rating =   movie.number_rating+1
       movie.save()
       serializer.save(watchlist = movie ,user_review =user)

class RewviewApi(viewsets.ModelViewSet):
    queryset =  Review.objects.all()
    serializer_class = ReviewSerializer
    #permission_classes =(IsAdminUserOrReadOnly ,)
    permission_classes =(ReviewReadOnly , )

class StreamApi(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer  
    
class WatchApi(viewsets.ModelViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer




'''
#@api_view(['GET','POST'])
#def movie_list_rest(request):
#    if request.method == 'GET':
#       movie = Movie.objects.all()
#       serializer_data = MovieSerializer(movie ,many = True) 
#       return Response(serializer_data.data)
#    
#    elif request.method == 'POST':
#        moveserialize =MovieSerializer(data=request.data)
#        if moveserialize.is_valid():
#            moveserialize.save()
#            return Response(moveserialize.data)
#        return Response(moveserialize.errors)    
#
#
#def get_object(id):
    try:
      return Movie.objects.get(pk =id)
    except :
        return Response("this Movie is not exist !")  
#
#@api_view(['GET','PUT','DELETE'])
#def movie_rest_pk(request ,id):
#    if request.method == 'GET':
#       movie = get_object(id)
#       serializer_data = MovieSerializer(movie) 
#       return Response(serializer_data.data)
#    
#    elif request.method == 'PUT':
#        movie = get_object(id)
#        moveserialize =MovieSerializer(movie ,data=request.data)
#        if moveserialize.is_valid():
#            moveserialize.save()
#            return Response(moveserialize.data)
#        return Response(moveserialize.errors)
#
#    elif request.method == 'PUT':
#        movie = get_object(id)
#        movie.delete()
#        return Response({movie.name:"deleted"})    
#
##third-party software       
'''

##########################################################################

@api_view(['POST',])
def regestration(request):
    if request.method == 'POST':
      userSerializer = RegisterSerializer(data=request.data)
      data = {}
      if userSerializer.is_valid():
            userdata = userSerializer.save()
            data["Response"] ="Registertion succesful !"
            data["username"] = userdata.username
            data["email"] =userdata.email
            #---- first method for create token ----# 
            ## token1 = Token.objects.create(user=userdata)
            ## print(token1.key)
            token = Token.objects.get(user=userdata)
            data["token"] = token.key
           
            return Response( data)
      return Response(userSerializer.errors) 


@api_view(['POST',])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response("log out yes ")
    return Response("log out no ")    