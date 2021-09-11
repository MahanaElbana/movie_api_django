from .models import Movie
from .serializer import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def movie_list_rest(request):
    if request.method == 'GET':
       movie = Movie.objects.all()
       serializer_data = MovieSerializer(movie ,many = True) 
       return Response(serializer_data.data)
    
    elif request.method == 'POST':
        moveserialize =MovieSerializer(data=request.data)
        if moveserialize.is_valid():
            moveserialize.save()
            return Response(moveserialize.data)
        return Response(moveserialize.errors)    


def get_object(id):
    try:
      return Movie.objects.get(pk =id)
    except :
        return Response("this Movie is not exist !")  

@api_view(['GET','PUT','DELETE'])
def movie_rest_pk(request ,id):
    if request.method == 'GET':
       movie = get_object(id)
       serializer_data = MovieSerializer(movie) 
       return Response(serializer_data.data)
    
    elif request.method == 'PUT':
        movie = get_object(id)
        moveserialize =MovieSerializer(movie ,data=request.data)
        if moveserialize.is_valid():
            moveserialize.save()
            return Response(moveserialize.data)
        return Response(moveserialize.errors)

    elif request.method == 'PUT':
        movie = get_object(id)
        movie.delete()
        return Response({movie.name:"deleted"})    

#third-party software         